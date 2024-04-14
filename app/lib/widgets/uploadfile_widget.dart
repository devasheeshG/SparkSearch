import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:get/get_connect/http/src/request/request.dart';
import 'package:http/http.dart' as http;
import 'package:path/path.dart';
import 'package:http_parser/http_parser.dart';
import 'package:file_picker/file_picker.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:spark/widgets/file_card.dart';

class FileUploadWidget extends StatefulWidget {
  @override
  _FileUploadWidgetState createState() => _FileUploadWidgetState();
}

class _FileUploadWidgetState extends State<FileUploadWidget> {
  File? _selectedFile;
  String? _filePath;

  void _selectFile() async {
    final result = await FilePicker.platform.pickFiles();
    if (result == null || result.files.isEmpty) return;
    setState(() {
      _selectedFile = File(result.files.single.path!);
      _filePath = result.files.single.path!;
    });
  }

  void _uploadFile(String? filePath) async {
    if (filePath == null) {
      print('No file selected.');
      return;
    }

    final fileStream = File(filePath).openRead();
    final SharedPreferences prefs = await SharedPreferences.getInstance();
    final String userId = prefs.getString('user_id') ?? 'empty';
    final Uri uri =
        Uri.parse('https://devel-8000.devasheeshmishra.com/api/upload_file');

    final request = http.MultipartRequest('POST', uri)
      ..headers['accept'] = 'application/json'
      ..fields['path'] = filePath
      ..fields['user_id'] = userId;
    print(filePath);
    print(userId);

    final fileExtension = extension(filePath).toLowerCase();
    MediaType? contentType;

    if (fileExtension == '.pdf') {
      contentType = MediaType('application', 'pdf');
    } else if (fileExtension == '.rtf') {
      contentType = MediaType('application', 'rtf');
    } else {
      print('Unsupported file type');
      return;
    }

    final file = http.MultipartFile.fromBytes(
      'file',
      await fileStream.toBytes(),
      filename: basename(filePath),
      contentType: contentType,
    );

    request.files.add(file);

    try {
      final response = await request.send();
      final reponse = await http.Response.fromStream(response);
      if (response.statusCode == 201) {
        print('File uploaded successfully.');
      } else {
        print('Failed to upload file. ${reponse.body}');
      }
    } catch (e) {
      print('Error uploading file: $e');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.white,
        appBar: AppBar(
          title: Text('File Upload'),
        ),
        body: Row(
          children: [
            Expanded(
                child: Container(
              decoration: BoxDecoration(
                  gradient: LinearGradient(
                colors: [Color(0xff9796f0), Color(0xfffbc7d4)],
                stops: [0, 1],
                begin: Alignment.bottomRight,
                end: Alignment.topLeft,
              )),
              child: ListView.builder(
                itemBuilder: (_, index) => Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: file_card(),
                ),
                itemCount: 4,
              ),
            )),
            Container(
              width: 300,
              color: Colors.transparent.withAlpha(12),
              child: Center(
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: <Widget>[
                    _selectedFile == null
                        ? Text('No file selected.')
                        : Text('Selected File: ${_selectedFile!.path}'),
                    SizedBox(height: 20),
                    ElevatedButton(
                      onPressed: _selectFile,
                      child: Text('Select File'),
                    ),
                    SizedBox(height: 20),
                    ElevatedButton(
                      onPressed: () {
                        if (_filePath != null) {
                          _uploadFile(_filePath);
                        } else {
                          print('No file selected.');
                        }
                      },
                      child: Text('Upload File'),
                    ),
                  ],
                ),
              ),
            )
          ],
        ));
  }
}

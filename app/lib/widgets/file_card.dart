import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:spark/uses/file/Selected_file.dart';

class file_card extends StatelessWidget {
//  Future<String?> jsonData=Fetch_file.file();
  @override
 Widget build(BuildContext context) {
    final parsedJson = json.decode("");
    final fileIds = List.from(parsedJson['file_ids']);

    return ListView.builder(
      itemCount: fileIds.length,
      itemBuilder: (context, index) {
        final fileId = fileIds[index];
        return ListTile(
          title: Text(fileId[2]), // Displaying the file name
          subtitle: Text(fileId[1]), // Displaying the file path
          trailing: Text(fileId[3].toUpperCase()), // Displaying the file type
        );
      },
    );
  }
}

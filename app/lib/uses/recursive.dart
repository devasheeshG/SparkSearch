import 'dart:io';
import 'package:path/path.dart' as path;

void readRichTextAndPdfFiles(String folderPath) async {
  final dir = Directory(folderPath);

  await for (var entity in dir.list(recursive: true, followLinks: false)) {
    final String filePath = entity.path;
    if (path.extension(filePath) == '.rtf' ||
        path.extension(filePath) == '.pdf') {
      try {
        final file = File(filePath);
        final text = await file.readAsString();
        // Convert the text from RTF/PDF to plain text here
        // You might need to use a package from pub.dev for this
        print('File: $filePath\nText: $text');
      } catch (e) {
        print('Error reading file $filePath: $e');
      }
    }
  }
}

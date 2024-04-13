import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';
import 'package:spark/main.dart';
import 'package:spark/screens/Login_Screen.dart';

class fetch_file {
  static Future<String?> file() async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    String Uid = prefs.getString('user_id') ?? "empty";

    final Uri url =
        Uri.parse('https://devel-8000.devasheeshmishra.com/api/get_file_ids');
    final request = http.MultipartRequest('POST', url);
    request.fields['user_id'] = Uid;

    final response = await request.send();
    if (response.statusCode == 200) {
      // Request successful

      print("successful fetch");

      // _handleResponse(context, resp);
      var rsponse = await http.Response.fromStream(response);
      print(rsponse);
      print(rsponse.body);
      return rsponse.body;
    }
  }
}

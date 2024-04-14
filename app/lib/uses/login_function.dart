import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';
import 'package:spark/main.dart';
import 'package:spark/screens/Login_Screen.dart';

class AuthService {
  static Future<void> registerUser(
      BuildContext context, String username, String password) async {
    final Uri url =
        Uri.parse('https://devel-8000.devasheeshmishra.com/api/auth/register');

    final request = http.MultipartRequest('POST', url);
    request.fields['username'] = username; // Set the form field 'username'
    request.fields['password'] = password; // Set the form field 'password'

    // Map<String, String> headers = {
    //   'Content-Type': 'application/json', // adjust content type as per your API
    //   // Add any other headers your API requires
    // };

    try {
      final response = await request.send();

      if (response.statusCode == 201) {
        // Request successful
        _handleResponse(context, response);
        print("successfull register ");
        Get.to(LoginScreen());
        // _handleResponse(context, resp);
        var rsponse = await http.Response.fromStream(response);
        print(rsponse);
      } else {
        // Request failed
        print('Request failed with status: ${response.statusCode}');
        //print(response.body);
        var rsponse = await http.Response.fromStream(response);
        print(rsponse);
      }
    } catch (e) {
      // Exception occurred
      print('Exception: $e');
    }
  }

  static Future<void> loginUser(
      BuildContext context, String username, String password) async {
    final Uri url =
        Uri.parse('https://devel-8000.devasheeshmishra.com/api/auth/login');

    final request = http.MultipartRequest('POST', url);
    request.fields['username'] = username; // Set the form field 'username'
    request.fields['password'] = password; // Set the form field 'password'
    SharedPreferences prefs = await SharedPreferences.getInstance();
    try {
      final response = await request.send();

      if (response.statusCode == 200) {
        // Request successful
        _handleResponse(context, response);
        print("successful login");
        Get.to(MyHomePage());
        // _handleResponse(context, resp);
        var rsponse = await http.Response.fromStream(response);
        print(rsponse);
        print(rsponse.body);
        Map<String, dynamic> jsonResponse = json.decode(rsponse.body);
        String userId = jsonResponse['user_id'];

        //  /---------------- //shared prefence(storage --------------------------------------------------------)

        prefs.setString('user_id', userId);
        print("Stored");

        String Uid = prefs.getString('user_id') ?? "empty";
        print(Uid);
      } else {
        // Request failed
        print('Request failed with status: ${response.statusCode}');
        var rsponse = await http.Response.fromStream(response);
        print(rsponse);
        //print(response.body);
        //print(response);
      }
    } catch (e) {
      // Exception occurred
      print('Exception: $e');
    }
  }

  static Logout() async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    prefs.remove('user_id');
  }

  static void _handleResponse(
      BuildContext context, http.StreamedResponse response) {
    if (response.statusCode == 201) {
      // Handle success
      _showDialog(context, 'Success', 'Operation was successful.');
    } else {
      // Handle failure
      _showDialog(context, 'Failure', 'Operation failed. Error: ${response}');
    }
  }

  static void _showDialog(BuildContext context, String title, String content) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text(title),
          content: Text(content),
          actions: <Widget>[
            TextButton(
              onPressed: () => Navigator.of(context).pop(),
              child: Text('OK'),
            ),
          ],
        );
      },
    );
  }
}

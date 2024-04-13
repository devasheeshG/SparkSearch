import 'package:flutter/material.dart';

import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:http/http.dart' as http;
import 'package:spark/main.dart';
import 'package:spark/uses/login_function.dart';

class LoginScreen extends StatelessWidget {
  final TextEditingController usernameController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();

  // void register(BuildContext context) async {
  //   final url =
  //       Uri.parse('https://devel-8000.devasheeshmishra.com/api/auth/register');

  //   final response = await http.post(
  //     url,
  //     headers: <String, String>{
  //       'Content-Type': 'application/json; charset=UTF-8',
  //     },
  //     body: jsonEncode({
  //       'username': usernameController.text.toString(),
  //       'password': passwordController.text.toString(),
  //     }),
  //   );

  //   if (response.statusCode >= 300) {
  //     // Registration successful, navigate to login screen
  //     showDialog(
  //       context: context,
  //       builder: (BuildContext context) {
  //         return AlertDialog(
  //           title: Text('Registration Failed'),
  //           content: Text('Failed to register user, User Exist.'),
  //           actions: [
  //             TextButton(
  //               onPressed: () => Navigator.pop(context),
  //               child: Text('OK'),
  //             ),
  //           ],
  //         );
  //       },
  //     );
  //   } else if (response.statusCode == 201) {
  //     // Registration failed, display error message

  //     print('successful');
  //     Navigator.push(
  //         context, MaterialPageRoute(builder: (context) => MyHomePage()));
  //   } else {
  //     print('success code is different.$response.statusCode');
  //   }
  // }

  // void register(BuildContext context) async {
  //   final url =
  //       Uri.parse('https://devel-8000.devasheeshmishra.com/api/auth/register');

  //   final response = await http.post(
  //     url,
  //     headers: <String, String>{
  //       'Content-Type': 'application; charset=UTF-8',
  //     },
  //     body: JsonCodec({
  //       'username': usernameController.text.toString(),
  //       'password': passwordController.text.toString(),
  //     }),,
  //   );

  //   if (response.statusCode >= 300) {
  //     // Registration successful, navigate to login screen
  //     showDialog(
  //       context: context,
  //       builder: (BuildContext context) {
  //         return AlertDialog(
  //           title: Text('Registration Failed'),
  //           content: Text('Failed to register user, User Exist.'),
  //           actions: [
  //             TextButton(
  //               onPressed: () => Navigator.pop(context),
  //               child: Text('OK'),
  //             ),
  //           ],
  //         );
  //       },
  //     );
  //   } else if (response.statusCode == 201) {
  //     // Registration failed, display error message

  //     print('successful');
  //     Navigator.push(
  //         context, MaterialPageRoute(builder: (context) => const MyHomePage()));
  //   } else {
  //     print('success code is different.$response.statusCode');
  //   }
  // }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        width: MediaQuery.of(context).size.width,
        decoration: BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
            colors: [
              const Color.fromARGB(255, 198, 173, 173),
              Colors.indigo,
              Colors.pinkAccent
            ],
          ),
        ),
        child: Center(
          child: Container(
            height: 600,
            width: 800,
            color: Colors.transparent.withOpacity(0.2),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                SizedBox(height: 50),
                Container(
                  height: 80,
                  width: 80,
                  child: Image(
                    fit: BoxFit.contain,
                    image: AssetImage("assets/icons/icon.png"),
                  ),
                ),
                SizedBox(height: 50),
                Padding(
                  padding: EdgeInsets.symmetric(horizontal: 40),
                  child: Container(
                    height: 50,
                    width: 400,
                    child: TextField(
                      controller: usernameController,
                      decoration: InputDecoration(
                        hintText: 'Username',
                        fillColor: Colors.white,
                        filled: true,
                        border: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(22),
                          borderSide: BorderSide.none,
                        ),
                      ),
                    ),
                  ),
                ),
                SizedBox(height: 20),
                Padding(
                  padding: EdgeInsets.symmetric(horizontal: 40),
                  child: Container(
                    height: 50,
                    width: 400,
                    child: TextField(
                      controller: passwordController,
                      obscureText: false,
                      decoration: InputDecoration(
                        hintText: 'Password',
                        fillColor: Colors.white,
                        filled: true,
                        border: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(22),
                          borderSide: BorderSide.none,
                        ),
                      ),
                    ),
                  ),
                ),
                SizedBox(height: 20),
                ElevatedButton(
                  onPressed: () => AuthService.loginUser(
                      context,
                      usernameController.text.toString(),
                      passwordController.text.toString()),
                  child: Text(
                    'Login',
                    style: TextStyle(color: Colors.white),
                  ),
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Color.fromARGB(255, 117, 164, 245),
                    padding: EdgeInsets.symmetric(horizontal: 40, vertical: 20),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(20),
                    ),
                  ),
                ),
                SizedBox(height: 20),
                Divider(),
                ElevatedButton(
                  onPressed: () => Get.back(),
                  child: Text(
                    'Register',
                    style: TextStyle(color: Colors.white),
                  ),
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.transparent,
                    padding: EdgeInsets.symmetric(horizontal: 40, vertical: 20),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(20),
                    ),
                  ),
                ),
                SizedBox(height: 20),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

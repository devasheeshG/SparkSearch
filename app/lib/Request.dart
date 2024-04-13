import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:http/http.dart' as http;

class request extends StatefulWidget {
  @override
  State<request> createState() => _requestState();
}

class _requestState extends State<request> {
  List<dynamic> user = [];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          ListView.builder(
              shrinkWrap: true,
              itemCount: 2,
              itemBuilder: (context, index) {
                // final usr = user[index];
                // final email = user[2];

                return ListTile(
                  title: Text("fsafj"),
                  subtitle: Text("sdkjf"),
                );
              }),
          SizedBox(
              height: 20), // Added spacing between the ListView and the button
          GestureDetector(
            onTap: () => fetch(), // Fixed the button size and spacing issue
            child: Container(
              height: 50,
              width: 150, // Adjusted the button width to 150
              color: Colors.blueAccent,
            ),
          )
        ],
      ),
    );
  }

  void fetch() async {
    print("working");
    const url = "https://fakerapi.it/api/v1/persons";
    final uri = Uri.parse(url);
    final response = await http.get(uri);
    final body = response.body;
    final json = jsonDecode(body);

    print(json['data']);
  }
}

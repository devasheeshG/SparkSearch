import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:spark/screens/chat_message.type.dart';
import 'package:spark/screens/chat_message_widget.dart';
//import 'package:openai/openai.dart';

class chatScreen extends StatefulWidget {
  @override
  State<chatScreen> createState() => _chatScreenState();
}

Future<String> getParticipant(String chatId, String participantId) async {
  final response = await http.get(Uri.parse(
      'https://api.freeapi.app/api/v1/chat-app/chats/group/$chatId/$participantId'));

  final body = json.decode(response.body) as Map;
  print(body);
  return """ Changes in teacher's salary is being discussed in below files:
1. postingid_20220286_dt_10042024 (Page 1)
2. postingid_20240056_dt_10042024 (Page 3)

Salary is increased from 1LPM to 1.3LPM""";
}

class _chatScreenState extends State<chatScreen> {
  final _textcontroller = TextEditingController();
  final _scrollController = ScrollController();
  final List<ChatMessage> _messages = [];
  late bool isLoading;
  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    isLoading = false;
  }

  void _scrollDown() {
    _scrollController.animateTo(_scrollController.position.maxScrollExtent,
        duration: Duration(milliseconds: 300), curve: Curves.easeOut);
  }

  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return Scaffold(
      body: Container(
        decoration: BoxDecoration(
            gradient: LinearGradient(
          colors: [Color(0xff9796f0), Color(0xfffbc7d4)],
          stops: [0, 1],
          begin: Alignment.bottomRight,
          end: Alignment.topLeft,
        )),
        child: Column(
          children: [
            Padding(
              padding: EdgeInsets.all(8),
              child: Row(
                children: [
                  Expanded(
                      child: Container(
                    height: 45,
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.all(Radius.circular(40)),
                    ),
                    child: TextField(
                      textCapitalization: TextCapitalization.sentences,
                      controller: _textcontroller,
                      decoration: InputDecoration(
                          hintText: 'Enter Your Prompt here',
                          fillColor: Color(0xffe7ecf2),
                          filled: true,
                          border: InputBorder.none,
                          focusedBorder: InputBorder.none,
                          enabledBorder: InputBorder.none,
                          disabledBorder: InputBorder.none),
                    ),
                  )),
                  Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: Visibility(
                        visible: !isLoading,
                        child: Container(
                          decoration: BoxDecoration(
                              color: Color.fromARGB(255, 133, 54, 235),
                              borderRadius: BorderRadius.circular(25)),
                          child: IconButton(
                            icon: Icon(
                              Icons.send,
                              color: Colors.white,
                            ),
                            onPressed: () async {
                              setState(() {
                                _messages.add(ChatMessage(
                                    text: _textcontroller.text,
                                    chatMessageType: ChatMessageType.use));

                                isLoading = true;
                              });
                              var input = _textcontroller.text;
                              _textcontroller.clear();
                              Future.delayed(Duration(microseconds: 50))
                                  .then((_) => _scrollDown());
                              getParticipant("asfkj", "jakek").then((value) {
                                setState(() {
                                  isLoading = false;
                                  _messages.add(ChatMessage(
                                      text: value,
                                      chatMessageType: ChatMessageType.bot));
                                });
                              });
                              _textcontroller.clear();
                              Future.delayed(Duration(milliseconds: 50))
                                  .then((_) => _scrollDown());
                            },
                          ),
                        )),
                  )
                ],
              ),
            ),
            Expanded(
                child: ListView.builder(
                    controller: _scrollController,
                    itemCount: _messages.length,
                    itemBuilder: (context, index) {
                      var message = _messages[index];
                      return Padding(
                        padding: const EdgeInsets.all(8.0),
                        child: chatMessageWidget(
                          text: message.text,
                          chatMessageType: message.chatMessageType,
                        ),
                      );
                    })),
            Visibility(
                visible: isLoading,
                child: Padding(
                  padding: EdgeInsets.all(8),
                  child: CircularProgressIndicator(
                    color: Colors.white,
                  ),
                )),
          ],
        ),
      ),
    );
  }
}

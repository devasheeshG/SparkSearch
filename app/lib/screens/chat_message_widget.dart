import 'package:flutter/material.dart';

import 'package:spark/screens/chat_message.type.dart';

class chatMessageWidget extends StatelessWidget {
  final String text;
  final ChatMessageType chatMessageType;
  chatMessageWidget({
    required this.text,
    required this.chatMessageType,
  });
  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return Container(
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(15),
        gradient: chatMessageType == ChatMessageType.bot
            ? LinearGradient(
                colors: [Color(0xffa811da), Color(0xffbf5ae0)],
                stops: [0, 1],
                begin: Alignment.bottomRight,
                end: Alignment.topLeft,
              )
            : LinearGradient(
                colors: [Colors.white, Colors.white10],
                stops: [0, 1],
                begin: Alignment.bottomRight,
                end: Alignment.topLeft,
              ),
      ),
      padding: EdgeInsets.all(16),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          chatMessageType == ChatMessageType.bot
              ? Container(
                  decoration:
                      BoxDecoration(borderRadius: BorderRadius.circular(16)),
                  margin: EdgeInsets.only(right: 36),
                  child: CircleAvatar(
                    child: Icon(Icons.mark_chat_unread_outlined),
                    backgroundColor: Color.fromARGB(255, 166, 56, 168),
                  ),
                )
              : Container(
                  margin: EdgeInsets.only(right: 16),
                  child: CircleAvatar(
                    child: Icon(Icons.person),
                    backgroundColor: const Color.fromARGB(255, 59, 58, 58),
                  ),
                ),
          Expanded(
              child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Container(
                padding: EdgeInsets.all(8),
                decoration:
                    BoxDecoration(borderRadius: BorderRadius.circular(18)),
                child: Text(
                  text,
                  style: TextStyle(fontSize: 12, color: Colors.white),
                ),
              )
            ],
          ))
        ],
      ),
    );
  }
}

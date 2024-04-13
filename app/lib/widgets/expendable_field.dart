import 'package:flutter/material.dart';

class ExpandableTextField extends StatefulWidget {
  @override
  _ExpandableTextFieldState createState() => _ExpandableTextFieldState();
}

class _ExpandableTextFieldState extends State<ExpandableTextField>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  late Animation<double> _widthAnimation;
  bool _isTextFieldFocused = false;
  bool _isHovered = false;
  TextEditingController _textController = TextEditingController();

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      vsync: this,
      duration: Duration(milliseconds: 300),
    );
    _widthAnimation = Tween<double>(
      begin: 50.0,
      end: 200.0,
    ).animate(CurvedAnimation(
      parent: _controller,
      curve: Curves.easeInOut,
    ));
    _textController.addListener(_onTextChanged);
  }

  @override
  void dispose() {
    _controller.dispose();
    _textController.dispose();
    super.dispose();
  }

  void _onTextFieldTapped() {
    setState(() {
      _isTextFieldFocused = true;
    });
    _controller.forward();
  }

  void _onTextFieldUnfocused() {
    setState(() {
      _isTextFieldFocused = false;
    });
    if (_textController.text.isEmpty && !_isHovered) {
      _controller.reverse();
    }
  }

  void _onTextChanged() {
    if (_textController.text.isNotEmpty) {
      setState(() {
        _isTextFieldFocused = true;
      });
    } else {
      if (!_isHovered) {
        _controller.reverse();
      }
    }
  }

  void _onMouseEnter(_) {
    setState(() {
      _isHovered = true;
    });
    if (!_isTextFieldFocused) {
      _controller.forward();
    }
  }

  void _onMouseExit(_) {
    setState(() {
      _isHovered = false;
    });
    if (_textController.text.isEmpty && !_isTextFieldFocused) {
      _controller.reverse();
    }
  }

  @override
  Widget build(BuildContext context) {
    double width = MediaQuery.of(context).size.width;

    return MouseRegion(
      onEnter: _onMouseEnter,
      onExit: _onMouseExit,
      child: AnimatedContainer(
        duration: Duration(milliseconds: 300),
        width: (_isTextFieldFocused || _isHovered)
            ? width * 1 / 1.5
            : width * 1 / 2,
        height: 50.0,
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(25.0),
          color: Colors.grey[200],
        ),
        padding: EdgeInsets.symmetric(horizontal: 16.0),
        child: Center(
          child: TextField(
            controller: _textController,
            decoration: InputDecoration(
                border: InputBorder.none, hintText: "Enter Your Promte here"),
            onTap: _onTextFieldTapped,
            onChanged: (text) => _onTextChanged(),
            onEditingComplete: _onTextFieldUnfocused,
            onSubmitted: (_) => _onTextFieldUnfocused,
          ),
        ),
      ),
    );
  }
}

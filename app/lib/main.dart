import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:get/get.dart';
import 'package:popover/popover.dart';
import 'package:sidebarx/sidebarx.dart';
import 'package:spark/request.dart';
import 'package:spark/screens/Login_Screen.dart';
import 'package:spark/screens/reg_screen.dart';
import 'package:spark/screens/chatScreen.dart';
import 'package:spark/uses/login_function.dart';
import 'package:spark/utils/colors/Colors.dart';
import 'package:spark/widgets/expendable_field.dart';
import 'package:spark/widgets/uploadfile_widget.dart';
//import 'package:spax_search/request%20and%20response/Request.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  onInit() {}

  @override
  Widget build(BuildContext context) {
    return GetMaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Flutter Demo',
      theme: ThemeData(
        primaryColor: SColors.primaryColor,
        canvasColor: SColors.canvasColor,
        scaffoldBackgroundColor: SColors.scaffoldBackgroundColor,
        textTheme: const TextTheme(
          headlineSmall: TextStyle(
            color: Colors.white,
            fontSize: 46,
            fontWeight: FontWeight.w800,
          ),
        ),
      ),
      home: RegisterScreen(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key}) : super(key: key);

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final _controller = SidebarXController(selectedIndex: 0, extended: true);
  final _key = GlobalKey<ScaffoldState>();

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Builder(builder: (context) {
        final isSmallScreen = MediaQuery.of(context).size.width < 600;
        return Scaffold(
            appBar: AppBar(
              title: Text(
                'SparKSearch ',
                style: TextStyle(fontWeight: FontWeight.bold),
              ),
              flexibleSpace: Container(
                decoration: BoxDecoration(
                    gradient: LinearGradient(
                  colors: [Color.fromARGB(255, 133, 54, 235), Colors.white],
                  stops: [0, 1],
                  begin: Alignment.bottomRight,
                  end: Alignment.topLeft,
                )),
              ),
            ),
            key: _key,
            drawer: SideBarXExample(
              controller: _controller,
            ),
            body: Row(
              children: [
                if (!isSmallScreen) SideBarXExample(controller: _controller),
                Expanded(
                    child: Center(
                  child: AnimatedBuilder(
                    animation: _controller,
                    builder: (context, child) {
                      switch (_controller.selectedIndex) {
                        case 0:
                          _key.currentState?.closeDrawer();
                          return Container(
                            child: Padding(
                              padding: const EdgeInsets.all(8.0),
                              child: Column(
                                mainAxisAlignment: MainAxisAlignment.start,
                                children: [
                                  SizedBox(
                                    height: 40,
                                  ),
                                  ExpandableTextField(),
                                ],
                              ),
                            ),
                          );
                        case 1:
                          _key.currentState?.closeDrawer();
                          return chatScreen();

                        case 2:
                          _key.currentState?.closeDrawer();
                          return FileUploadWidget();
                        default:
                          return Center(
                            child: Text(
                              'User',
                              style:
                                  TextStyle(color: Colors.white, fontSize: 40),
                            ),
                          );
                      }
                    },
                  ),
                ))
              ],
            ));
      }),
    );
  }
}

class SideBarXExample extends StatelessWidget {
  const SideBarXExample({Key? key, required SidebarXController controller})
      : _controller = controller,
        super(key: key);
  final SidebarXController _controller;

  void showPopupMenu(BuildContext context) {
    final RenderBox bar = context.findRenderObject() as RenderBox;
    final Offset target = bar.localToGlobal(Offset.zero);

    showMenu(
      context: context,
      position: RelativeRect.fromLTRB(target.dx, target.dy,
          target.dx + bar.size.width, target.dy + bar.size.height),
      items: <PopupMenuEntry>[
        PopupMenuItem(
          child: Text('Option 1'),
          onTap: () {
            // Handle option 1
          },
        ),
        PopupMenuItem(
          child: Text('Option 2'),
          onTap: () {
            // Handle option 2
          },
        ),
        // Add more options as needed
      ],
    );
  }

  @override
  Widget build(BuildContext context) {
    return SidebarX(
      controller: _controller,
      theme: const SidebarXTheme(
        selectedIconTheme: IconThemeData(color: Colors.white),
        textStyle: TextStyle(
            color: Colors.black,
            fontWeight: FontWeight.w800,
            fontFamily: 'poppins'),
        selectedItemDecoration: BoxDecoration(
            color: Color.fromARGB(255, 133, 54, 235),
            borderRadius: BorderRadius.all(
              Radius.circular(14),
            ),
            boxShadow: [
              BoxShadow(
                  color: Color.fromARGB(255, 245, 130, 205),
                  offset: Offset.zero,
                  spreadRadius: 0.4,
                  blurRadius: 1)
            ]),
        //padding: EdgeInsets.all(20),
        decoration: BoxDecoration(
          color: Color(0xffe7ecf2),
        ),
        iconTheme: IconThemeData(
          color: Colors.black,
        ),
        selectedTextStyle:
            const TextStyle(color: Colors.white, fontWeight: FontWeight.bold),
      ),
      extendedTheme: const SidebarXTheme(width: 250),
      //  footerDivider: Divider(color: Colors.white.withOpacity(0.8), height: 1),

      headerBuilder: (context, extended) {
        return const SizedBox(
            height: 100,
            child: Positioned(
              left: 20,
              child: Text(
                "Chats",
                style: TextStyle(fontSize: 30, fontWeight: FontWeight.bold),
              ),
            ));
      },
      items: const [
        SidebarXItem(
          icon: Icons.home,
          label: '  Home',
        ),
        SidebarXItem(icon: Icons.chat, label: '  Chat'),
        //SidebarXItem(icon: Icons.settings, label: '  Upload'),
        //SidebarXItem(icon: Icons.dark_mode, label: ' +  New chat'),
        SidebarXItem(
          icon: Icons.dark_mode,
          label: ' Files and Upload',
        ),
      ],
    );
  }
}

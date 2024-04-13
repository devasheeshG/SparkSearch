import React from 'react';
import { FaApple, FaWindows, FaAndroid } from 'react-icons/fa';

const InstallButton = () => {
  const handleClick = () => {
    // Detect the user's operating system
    const userAgent = window.navigator.userAgent;
    let downloadUrl;
    if (/(Mac|iPhone|iPod|iPad)/i.test(userAgent)) {
      // User is on macOS, iOS, or iPadOS
      downloadUrl = 'https://devel-8000.devasheeshmishra.com/api/download_app?platform=mac';
    } else if (/Android/i.test(userAgent)) {
      // User is on Android
      downloadUrl = 'https://devel-8000.devasheeshmishra.com/api/download_app?platform=android';
    } else if (/(Windows|Win32|Win64|WinCE)/i.test(userAgent)) {
      // User is on Windows
      downloadUrl = 'https://devel-8000.devasheeshmishra.com/api/download_app?platform=windows';
    } else {
      // Unknown operating system
      alert('Your operating system is not supported. Please contact us for assistance.');
      return;
    }
    // Initiate the download
    window.location.href = downloadUrl;
  };

  return (
    <div className="flex items-center">
      <button
        onClick={handleClick}
        className="bg-white hover:bg-blue-100 text-black font-bold py-2 px-4 rounded flex items-center space-x-2"
      >
        <span>Install Now</span>
        {/(Mac|iPhone|iPod|iPad)/i.test(window.navigator.userAgent) && (
          <FaApple className="text-gray-800" size={20} />
        )}
        {/(Windows|Win32|Win64|WinCE)/i.test(window.navigator.userAgent) && (
          <FaWindows className="text-gray-800" size={20} />
        )}
        {/Android/i.test(window.navigator.userAgent) && (
          <FaAndroid className="text-gray-800" size={20} />
        )}
      </button>
    </div>
  );
};

const Navbar = () => {
  return (
    <nav className="bg-purple-900 bg-opacity-80 h-[fit-content] w-full flex justify-between px-10 py-2 sticky top-0">
      <div className="flex items-center">
        <a href="/" className="text-white hover:opacity-50 mr-4 font-bold text-lg">
          Home
        </a>
        <div className="logo h-auto w-16">
          <a href="/">
            <img
              className="h-auto w-16"
              src="/Untitled_design__2_-removebg-preview.png"
              alt=""
            />
          </a>
        </div>
      </div>
      <div className="right_container mx-2 text-white my-auto flex space-x-10 items-center">
        <ul className="flex space-x-8">
          <li className="hover:opacity-50 font-bold text-lg">
            <a href="/features">Features</a>
          </li>
          <li className="hover:opacity-50 font-bold text-lg">
            <a href="https://github.com/devasheeshG/SparkSearch">Docs</a>
          </li>
          <li className="hover:opacity-50 font-bold text-lg">
            <a href="/youtube">Youtube</a>
          </li>
          <li className="hover:opacity-50 font-bold text-lg">
            <a href="/contact">Contact</a>
          </li>
        </ul>
        <InstallButton />
      </div>
    </nav>
  );
};

export default Navbar;
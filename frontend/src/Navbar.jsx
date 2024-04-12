import React from 'react';

const Navbar = () => {
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
    <nav className="bg-black h-[fit-content] w-full flex justify-between px-10 py-2 sticky top-0">
      <div className="logo h-auto w-16">
        <a href="/">
          <img className="h-auto w-16" src="icon.png" alt="" />
        </a>
      </div>
      <div className="right_container mx-2 text-white my-auto flex space-x-10 items-center">
        <ul className="flex space-x-8 ">
          <li className="hover:opacity-50">
            <a href="/features">Features</a>
          </li>
          <li className="hover:opacity-50">
            <a href="/docs">Docs</a>
          </li>
          <li className="hover:opacity-50">
            <a href="/youtube">Youtube</a>
          </li>
          <li className="hover:opacity-50">
            <a href="/contact">Contact</a>
          </li>
        </ul>
        <button onClick={handleClick} className="bg-white hover:bg-blue-100 text-black font-bold py-2 px-4 rounded">
          Install Now
        </button>
      </div>
    </nav>
  );
};

export default Navbar;
import React from 'react';
import { FaGoogle, FaLinkedin, FaYoutube, FaGithub } from 'react-icons/fa';

function Footer() {
  return (
    <footer className="text-black py-6 px-16 border border-black">
      <div className="container mx-auto flex justify-between items-center">
        <div>
          <h3 className="text-lg font-bold mb-2">Contact Details:</h3>
          <ul>
            <li>Email: sharmavs9205@gmail.com</li>
            <li>Phone: 7303876390</li>
          </ul>
        </div>
        <div>
          <h3 className="text-lg font-bold mb-2">Social Media:</h3>
          <ul className="flex space-x-4">
            <li>
              <a href="https://www.linkedin.com/in/vishal-sharma-368513258/" target="_blank" rel="noopener noreferrer">
                <FaLinkedin className="text-white hover:text-blue-500 transition duration-300" size={24} />
              </a>
            </li>
            <li>
              <a href="https://www.youtube.com" target="_blank" rel="noopener noreferrer">
                <FaYoutube className="text-white hover:text-blue-500 transition duration-300" size={24} />
              </a>
            </li>
            <li>
              <a href="https://github.com/devasheeshG/SparkSearch" target="_blank" rel="noopener noreferrer">
                <FaGithub className="text-white hover:text-blue-500 transition duration-300" size={24} />
              </a>
            </li>
            {/* Add more social media icons as needed */}
          </ul>
        </div>
      </div>
    </footer>
  );
}

export default Footer;

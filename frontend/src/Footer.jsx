import React from 'react';
import { FaLinkedin, FaYoutube, FaGithub } from 'react-icons/fa';

function Footer() {
  return (
    <footer className="bg-gray-800 text-white py-8 px-4 sm:px-6 lg:px-8">
      <div className="container mx-auto flex flex-col md:flex-row justify-between items-center">
        <div className="mb-6 md:mb-0">
          <h3 className="text-2xl font-bold mb-2">Contact Details</h3>
          <ul>
            <li>xxx@gmail.com</li>
            <li>+91 XXXXXXXXXX</li>
          </ul>
        </div>
        <div>
          <ul className="flex space-x-4">
            <li>
              <a
                href="https://www.linkedin.com/in/vishal-sharma-368513258/"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-block bg-white text-blue-500 hover:text-blue-700 rounded-full p-2 transition-colors duration-300"
              >
                <FaLinkedin size={24} />
              </a>
            </li>
            <li>
              <a
                href="https://www.youtube.com"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-block bg-white text-red-500 hover:text-blue-500 rounded-full p-2 transition-colors duration-300"
              >
                <FaYoutube size={24} />
              </a>
            </li>
            <li>
              <a
                href="https://github.com/devasheeshG/SparkSearch"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-block bg-white text-gray-800 hover:text-blue-500 rounded-full p-2 transition-colors duration-300"
              >
                <FaGithub size={24} />
              </a>
            </li>
          </ul>
        </div>
      </div>
    </footer>
  );
}

export default Footer;
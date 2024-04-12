import React from 'react';

function Contact() {
  const teamMembers = [
    {
      name: 'Vishal Sharma',
      linkedin: 'https://www.linkedin.com/in/vishal-sharma-368513258/',
      github: 'https://github.com/vishalsharma',
    },
    {
      name: 'Devasheesh Mishra',
      linkedin: 'https://www.linkedin.com/in/devasheeshmishra/',
      github: 'https://github.com/devasheeshmishra',
    },
    {
      name: 'Aryan Kaushik',
      linkedin: 'https://www.linkedin.com/in/aryankaushik/',
      github: 'https://github.com/aryankaushik',
    },
    {
      name: 'Rohan Bharadwaj',
      linkedin: 'https://www.linkedin.com/in/rohanbharadwaj/',
      github: 'https://github.com/rohanbharadwaj',
    },
  ];

  return (
    <div className="bg-gray-100 py-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-3xl font-bold text-center text-gray-800 mb-8 font-tilt-neon">
          Meet Our Talented Team
        </h1>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {teamMembers.map((member, index) => (
            <div
              key={index}
              className="bg-white shadow-md rounded-lg p-6 transition-transform duration-300 hover:scale-105"
            >
              <h2 className="text-2xl font-semibold text-gray-800 mb-2">
                {member.name}
              </h2>
              <div className="flex items-center mb-4">
                {member.linkedin && (
                  <a
                    href={member.linkedin}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-blue-500 hover:text-blue-700 mr-4"
                  >
                    LinkedIn
                  </a>
                )}
                {member.github && (
                  <a
                    href={member.github}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-gray-700 hover:text-gray-900"
                  >
                    GitHub
                  </a>
                )}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default Contact;
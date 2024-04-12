import React from 'react';

function Contact() {
  const teamMembers = [
    {
      name: 'Vishal Sharma',
      linkedin: '',
      github: 'https://github.com/johndoe'
    },
    {
      name: 'Devasheesh mishra',
      linkedin: 'https://www.linkedin.com/in/janesmith/',
      github: 'https://github.com/janesmith'
    },
    {
      name: 'Aryan Kaushik',
      linkedin: 'https://www.linkedin.com/in/michaeljohnson/',
      github: 'https://github.com/michaeljohnson'
    },
    {
      name: 'Rohan Bharadwaj',
      linkedin: 'https://www.linkedin.com/in/emilywilliams/',
      github: 'https://github.com/emilywilliams'
    },
    {
      name: 'Vipin',
      linkedin: 'https://www.linkedin.com/in/emilywilliams/',
      github: 'https://github.com/emilywilliams'
    }
  ];

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Meet Our Team</h1>
      <div className="grid grid-cols-2 gap-4">
        {teamMembers.map((member, index) => (
          <div key={index} className="border p-4 rounded-md">
            <h2 className="text-xl font-semibold mb-2">{member.name}</h2>
            <p>
              <strong>LinkedIn:</strong>{' '}
              <a href={member.linkedin} target="_blank" rel="noopener noreferrer">{member.name}'s LinkedIn Profile</a>
            </p>
            <p>
              <strong>GitHub:</strong>{' '}
              <a href={member.github} target="_blank" rel="noopener noreferrer">{member.name}'s GitHub Profile</a>
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Contact;

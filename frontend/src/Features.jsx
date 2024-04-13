import React from 'react';

export default function Features() {
  return (
    <div className="bg-gray-100 py-16">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-4xl font-extrabold text-center text-gray-800 mb-12 font-tilt-neon">
          Unlock the Power of SparkSearch
        </h1>
        <div className="flex justify-center items-center space-x-4 ">
          <div className="bg-white shadow-md rounded-lg p-6 transition-transform duration-300 hover:scale-105 w-[28.3vw]">
            <div className="flex items-center mb-4">
              <svg
                className="h-8 w-8 text-blue-500 mr-4"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
                <polyline points="7 10 12 15 17 10" />
                <line x1="12" y1="15" x2="12" y2="3" />
              </svg>
              <h3 className="text-2xl font-semibold text-gray-800">
                Contextual Search
              </h3>
            </div>
            <p className="text-gray-600 mb-4 text-xl text-center" style={{ wordSpacing: '1.3px' }}>
              Leverage advanced algorithms that understand the true meaning and
              intent behind your queries, delivering tailored results that
              match your specific needs.
            </p>
          </div>
          <div className="bg-white shadow-md rounded-lg p-6 transition-transform duration-300 hover:scale-105 w-[30vw]">
            <div className="flex items-center mb-4">
              <svg
                className="h-8 w-8 text-blue-500 mr-4"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z" />
                <circle cx="12" cy="10" r="3" />
              </svg>
              <h3 className="text-2xl font-semibold text-gray-800 ">
                Personalized Experience
              </h3>
            </div>
            <p className="text-gray-600 mb-4 text-xl text-center" style={{ wordSpacing: '1.3px' }}>
              SparkSearch adapts to your unique preferences and data structures,
              ensuring a seamless and efficient search experience tailored to
              your needs.
            </p>
          </div>
          <div className="bg-white shadow-md rounded-lg p-6 transition-transform duration-300 hover:scale-105 w-[28.3vw]">
            <div className="flex items-center mb-4">
              <svg
                className="h-8 w-8 text-blue-500 mr-4"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z" />
                <polyline points="3.27 6.96 12 12.01 20.73 6.96" />
                <line x1="12" y1="22.08" x2="12" y2="12" />
              </svg>
              <h3 className="text-2xl font-semibold text-gray-800">
                Seamless Integration
              </h3>
            </div>
            <p className="text-gray-600 mb-4 text-xl text-center " style={{ wordSpacing: '1.3px' }}>
              SparkSearch seamlessly integrates with your existing data sources,
              eliminating the need for external uploads and providing a
              streamlined search experience.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

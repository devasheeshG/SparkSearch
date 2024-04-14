import React from 'react';

export default function Youtube() {
  return (
    <div className="bg-gray-100 py-16">
      <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-4xl font-bold text-center text-gray-800 mb-8 font-tilt-neon">
          Experience SparkSearch in Action
        </h1>
        <div className="relative pt-[56.25%] rounded-lg overflow-hidden">
          <video
            autoPlay
            loop
            controls={false}
            muted
            controlsList="nodownload noremoteplayback"
            className="absolute top-0 left-0 w-full h-full object-cover"
          >
            <source
              src="/preview.mp4"
              type="video/mp4"
            />
            Your browser does not support the video tag.
          </video>
        </div>
        <div className="mt-8 text-center">
          <p className="text-lg text-gray-600">
            Witness the power of contextual search and personalized data
            exploration in our demo video.
          </p>
        </div>
      </div>
    </div>
  );
}
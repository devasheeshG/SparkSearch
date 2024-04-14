import React from 'react';
import Typed from 'typed.js';
import Footer from './Footer';

export default function Content() {
  // Create reference to store the DOM element containing the animation
  const el = React.useRef(null);

React.useEffect(() => {
  const typed = new Typed(el.current, {
    strings: [
      'Revolutionize archaic lexicon substitution with contextual exploration for personalized data curation',
    ],
    typeSpeed: 30,
    loop: true,
  });

  return () => {
    // Destroy Typed instance during cleanup to stop animation
    typed.destroy();
  };
}, []);
  

  return (
    <div>
      <div className="py-16 px-4 bg-gray-100">
        <div className="text-6xl font-bold text-gray-700 flex justify-center items-center">
          Say hello to SparkSearch
        </div>
        <div className="text-4xl py-6 px-2 font-bold text-purple-600 flex justify-center items-center">
  <div className="text-center">
    <span ref={el} />
  </div>
</div>
        <div className="text-2xl py-4 font-semibold text-gray-600 text-center px-10">
          In today's fast-paced world, the need for efficient and effective data
          search has become crucial. Introducing SparkSearch, an innovative
          application that empowers users to move beyond the limitations of
          conventional search and embrace the power of contextual searching for
          their own data.
        </div>
      </div>
      <div className="py-8 px-4 border border-gray-400 rounded-[20px] w-[fit-content] mx-auto flex space-x-1 h-[90vh]">
        <video
          autoPlay
          loop
          controls={false}
          muted
          controlsList="nodownload noremoteplayback"
          className="border rounded-[20px] h-[80vh] mx-auto"
        >
          <source
            src="/preview.mp4"
            type="video/mp4"
          />
          Your browser does not support the video tag.
        </video>
      </div>
      <div className="my-10 py-8 px-16 flex justify-around items-center bg-gray-800 text-white">
        <div className="flex-1 mr-8">
          <div className="font-semibold text-gray-400 text-2xl mt-4">
          Personalized. Contextual. Seamless.
          </div>
          <div className="font-bold text-white text-5xl mt-4">
            Get Work Done with SparkSearch
          </div>
          <div className="font-semibold text-2xl text-gray-300 mt-4">
          SparkSearch revolutionizes data search by leveraging contextual exploration, enabling users to efficiently navigate and curate their personal data with unprecedented precision and ease.
          </div>
        </div>
        <div className="flex-1">
          <img
            src="/robo.png"
            alt=""
            className="rounded-[20px] w-full max-w-[400px]"
          />
        </div>
      </div>
      <Footer />
    </div>
  );
}
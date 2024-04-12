import React from 'react'
import Typed from 'typed.js';

export default function Content() {
    // Create reference to store the DOM element containing the animation
  const el = React.useRef(null);

  React.useEffect(() => {
    const typed = new Typed(el.current, {
      strings: [`Revolutionize archaic lexicon substitution with contextual exploration for personalized data curation`],
      typeSpeed: 30,
      loop:true,
    });

    return () => {
      // Destroy Typed instance during cleanup to stop animation
      typed.destroy();
    };
  }, []);
  return (
    <div>
      <div className='py-16 px-4'>
        <div className="text-3xl font-bold text-gray-700 flex justify-center items-center ">Developers, say hello to...</div>
        <div className="text-2xl py-6 px-2 font-bold text-purple-700 flex justify-center items-center "><span ref={el} /></div>
        <div className="text-sm py-4 font-semibold text-brown-400 flex justify-center items-center px-10">
        Pieces is your AI-enabled productivity tool designed to supercharge developer efficiency. Unify your entire toolchain with an on-device copilot that helps you capture, enrich, and reuse useful materials, streamline collaboration, and solve complex problems through a <br />contextual understanding of your workflow.</div>
      </div>
      <div className="px-4 ">
      <video autoPlay={true} loop controls={false} muted controlsList="nodownload noremoteplayback" className='border rounded-[20px] h-[100vh] mx-auto'>
        <source src="https://file-examples.com/storage/feed2327706616bd9a07caa/2017/04/file_example_MP4_480_1_5MG.mp4" type="video/mp4" />
        Your browser does not support the video tag.
      </video>
      </div>
    </div>
  )
}

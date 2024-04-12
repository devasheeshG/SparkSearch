import React from 'react';

const Navbar = () => {
  const handleClick = () => {
    alert('Button clicked!');
  };
  return (
    <nav className=" bg-black h-[fit-content] w-full flex justify-between px-10 py-2 sticky top-0">
    <div className="logo h-auto w-16"><a href="/"><img className="h-auto w-16" src="/public/Untitled_design__2_-removebg-preview.png" alt="" /></a></div>
    <div className="right_container mx-2 text-white my-auto flex space-x-10 items-center">
     <ul className='flex space-x-8 '>
      <li className='hover:opacity-50'>
        <a href="/features">Features</a>
      </li>
      <li className='hover:opacity-50'>
        <a href="https://github.com/devasheeshG/SparkSearch">Docs</a>
      </li>
      <li className='hover:opacity-50'>
        <a href="/youtube">Youtube</a>
      </li>
      <li className='hover:opacity-50'>
        <a href="/contact">Contact</a>
      </li>
     </ul>
     <button
      onClick={handleClick}
      className="bg-white hover:bg-blue-100 text-black font-bold py-2 px-4 rounded"
    > 
    Install Now
    </button>
    </div>
 </nav>
  );
}

export default Navbar;

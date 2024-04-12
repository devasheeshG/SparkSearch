import React from 'react'

export default function Youtube() {
  return (
    <div className='h-[90vh]'>
     <video autoPlay={true} loop controls={false} muted controlsList="nodownload noremoteplayback" className='border rounded-[20px] h-[80vh] mx-auto '>
        <source src="https://file-examples.com/storage/feed2327706616bd9a07caa/2017/04/file_example_MP4_480_1_5MG.mp4" type="video/mp4" />
        Your browser does not support the video tag.
      </video>
    </div>
  )
}

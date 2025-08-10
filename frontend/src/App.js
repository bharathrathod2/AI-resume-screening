import React from 'react'
import UploadForm from './components/UploadForm'

function App(){
  return (
    <div className="p-4 max-w-3xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">AI Resume Screener</h1>
      <UploadForm />
    </div>
  )
}

export default App
import React, {useState} from 'react'
import axios from 'axios'

export default function UploadForm(){
  const [file, setFile] = useState(null)
  const [jd, setJd] = useState('')
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)

  const submit = async e => {
    e.preventDefault()
    const form = new FormData()
    form.append('job_description', jd)
    if(file) form.append('resume', file)
    setLoading(true)
    try{
      const res = await axios.post('http://localhost:5000/api/score', form)
      setResult(res.data)
    }catch(err){
      alert('Error: ' + (err?.response?.data?.error || err.message))
    }finally{ setLoading(false) }
  }

  return (
    <form onSubmit={submit} className="space-y-3">
      <div>
        <label className="block">Job Description</label>
        <textarea value={jd} onChange={e=>setJd(e.target.value)} rows={6} className="w-full" />
      </div>
      <div>
        <label>Resume (PDF/DOCX)</label>
        <input type="file" accept=".pdf,.doc,.docx" onChange={e=>setFile(e.target.files[0])} />
      </div>
      <button type="submit" disabled={loading}>{loading ? 'Scoring...' : 'Score Resume'}</button>

      {result && (
        <div className="mt-4">
          <h3>Match score: {result.match_score}</h3>
          <p>Matched: {JSON.stringify(result.matched_skills)}</p>
          <p>Missing: {JSON.stringify(result.missing_skills)}</p>
          <pre>{JSON.stringify(result.top_resume_phrases, null, 2)}</pre>
        </div>
      )}
    </form>
  )
}
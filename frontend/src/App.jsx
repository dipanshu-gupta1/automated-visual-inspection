import { useState } from 'react'
import './App.css'

function App() {
  const [result, setResult] = useState(null)

  // This function runs when you pick a file
  const handleUpload = async (event) => {
    const file = event.target.files[0]
    if (!file) return

    // Package the picture up in a digital envelope
    const formData = new FormData()
    formData.append('file', file)

    try {
      // 📞 Call the Python Delivery Person on the walkie-talkie!
      const response = await fetch('http://127.0.0.1:8000/upload-image/', {
        method: 'POST',
        body: formData
      })

      // Read the note Python sent back
      const data = await response.json()
      setResult(data) // Save it to the screen!

    } catch (error) {
      console.error("The Walkie-Talkie broke:", error)
    }
  }

  return (
    <div>
      <h1>🏭 Smart Factory Inspector</h1>
      <p>Upload a picture to check for defects:</p>

      {/* The Upload Button */}
      <input type="file" onChange={handleUpload} />

      {/* If we get a result back from Python, show this box! */}
      {result && (
        <div style={{ marginTop: '30px', padding: '20px', border: '3px solid #4CAF50', borderRadius: '10px' }}>
          <h2>✅ Inspection Complete!</h2>
          <p><strong>The AI Saw:</strong> {result.ai_saw}</p>
          <p><strong>Confidence:</strong> {result.confidence}</p>
          <p><strong>Saved to Diary ID:</strong> {result.database_id}</p>
        </div>
      )}
    </div>
  )
}

export default App
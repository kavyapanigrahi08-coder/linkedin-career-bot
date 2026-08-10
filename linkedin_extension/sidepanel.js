document.getElementById('runBtn').addEventListener('click', async () => {
  const task = document.getElementById('taskSelect').value;
  const targetRole = document.getElementById('targetRole').value;
  const studentDegree = document.getElementById('studentDegree').value;
  const userInput = document.getElementById('userInput').value;
  
  const outputDiv = document.getElementById('output');
  const spinner = document.getElementById('loadingSpinner');

  spinner.style.display = 'block';
  outputDiv.innerText = '';

  try {
    const response = await fetch('http://127.0.0.1:8000/api/assistant', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        task: task,
        user_input: userInput,
        session_memory: {
          target_role: targetRole,
          education: studentDegree
        }
      })
    });

    const data = await response.json();
    spinner.style.display = 'none';

    if (data.success) {
      outputDiv.innerText = data.result;
    } else {
      outputDiv.innerText = "Error: " + (data.detail || "Failed to process request.");
    }
  } catch (err) {
    spinner.style.display = 'none';
    outputDiv.innerText = "⚠️ Connection Error!\nMake sure server.py is running in your terminal (http://127.0.0.1:8000).";
  }
});

document.getElementById('copyBtn').addEventListener('click', () => {
  const text = document.getElementById('output').innerText;
  if (text && !text.startsWith("Results will appear") && !text.startsWith("⚠️ Connection Error")) {
    navigator.clipboard.writeText(text);
    const copyBtn = document.getElementById('copyBtn');
    copyBtn.innerText = "✅ Copied!";
    setTimeout(() => { copyBtn.innerText = "📋 Copy Result to Clipboard"; }, 2000);
  }
});
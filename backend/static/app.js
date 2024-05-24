document.getElementById('register-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const username = document.getElementById('register-username').value;
    const email = document.getElementById('register-email').value;
    const password = document.getElementById('register-password').value;

    const response = await fetch('/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, email, password }),
    });

    if (response.ok) {
        alert('Registration successful!');
    } else {
        alert('Registration failed');
    }
});

document.getElementById('login-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;

    const response = await fetch('/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password }),
    });

    if (response.ok) {
        alert('Login successful!');
        document.getElementById('auth-section').style.display = 'none';
        document.getElementById('upload-section').style.display = 'block';
        document.getElementById('logout-button').style.display = 'block';
    } else {
        alert('Login failed');
    }
});

document.getElementById('logout-button').addEventListener('click', async () => {
    const response = await fetch('/logout', {
        method: 'GET',
    });

    if (response.ok) {
        alert('Logout successful!');
        document.getElementById('auth-section').style.display = 'block';
        document.getElementById('upload-section').style.display = 'none';
        document.getElementById('logout-button').style.display = 'none';
    } else {
        alert('Logout failed');
    }
});

document.getElementById('upload-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const fileInput = document.getElementById('file-input');
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    const response = await fetch('/upload', {
        method: 'POST',
        body: formData,
    });

    if (response.ok) {
        const blob = await response.blob();
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = 'output.pdf';
        link.click();
    } else {
        alert('File upload failed');
    }
});

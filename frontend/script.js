const baseUrl = 'http://localhost:5000'; // Update with your Flask app URL

// Function to fetch and display users
async function fetchUsers() {
    const response = await axios.get(`${baseUrl}/users`);
    const userList = document.getElementById('userList');
    userList.innerHTML = ''; // Clear existing list

    response.data.forEach(user => {
        const listItem = document.createElement('li');
        listItem.innerHTML = `
            <strong>ID:</strong> ${user.id} |
            <strong>Name:</strong> ${user.name} |
            <strong>Email:</strong> ${user.email} |
            <button onclick="updateUser(${user.id})">Update</button> |
            <button onclick="deleteUser(${user.id})">Delete</button>
        `;
        userList.appendChild(listItem);
    });

    // Populate the user dropdown in the zoo entity form
    const entityUserSelect = document.getElementById('entityUser');
    entityUserSelect.innerHTML = '<option value="" disabled selected>Select User</option>';

    response.data.forEach(user => {
        const option = document.createElement('option');
        option.value = user.id;
        option.text = `${user.name} (${user.email})`;
        entityUserSelect.appendChild(option);
    });
}

// Function to add a new user
async function addUser(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);

    await axios.post(`${baseUrl}/users`, {
        name: formData.get('name'),
        email: formData.get('email')
    });

    form.reset();
    fetchUsers(); // Refresh the user list
}

// Function to update a user
async function updateUser(userId) {
    const newName = prompt('Enter new name:');
    const newEmail = prompt('Enter new email:');

    await axios.put(`${baseUrl}/users/${userId}`, {
        name: newName,
        email: newEmail
    });

    fetchUsers(); // Refresh the user list
}

// Function to delete a user
async function deleteUser(userId) {
    const confirmDelete = confirm('Are you sure you want to delete this user?');
    if (confirmDelete) {
        await axios.delete(`${baseUrl}/users/${userId}`);
        fetchUsers(); // Refresh the user list
    }
}

async function fetchEntities() {
    const response = await axios.get(`${baseUrl}/zoo`);
    const entityList = document.getElementById('entityList');
    entityList.innerHTML = ''; // Clear existing list

    response.data.forEach(entity => {
        const listItem = document.createElement('li');
        listItem.innerHTML = `
            <strong>ID:</strong> ${entity.id} |
            <strong>Color:</strong> ${entity.color} |
            <strong>Age:</strong> ${entity.age} |
            <strong>Image:</strong> <img src="${baseUrl}/uploads/${entity.image}" alt="Entity Image" width="50"> |
            <strong>User ID:</strong> ${entity.user_id} |
            <button onclick="updateEntity(${entity.id})">Update</button> |
            <button onclick="deleteEntity(${entity.id})">Delete</button>
        `;
        entityList.appendChild(listItem);
    });
}

// Function to add a new zoo entity
async function addEntity(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);

    await axios.post(`${baseUrl}/zoo`, formData);

    form.reset();
    fetchEntities(); // Refresh the entity list
}


// Function to update a zoo entity
async function updateEntity(entityId) {
    const newColor = prompt('Enter new color:');
    const newAge = prompt('Enter new age:');
    const newImage = prompt('Enter new image URL:');

    await axios.put(`${baseUrl}/zoo/${entityId}`, {
        color: newColor,
        age: parseInt(newAge),
        image: newImage
    });

    fetchEntities(); // Refresh the entity list
}

// Function to delete a zoo entity
async function deleteEntity(entityId) {
    const confirmDelete = confirm('Are you sure you want to delete this zoo entity?');
    if (confirmDelete) {
        await axios.delete(`${baseUrl}/zoo/${entityId}`);
        fetchEntities(); // Refresh the entity list
    }
}

// Attach event listeners to the forms
document.getElementById('addUserForm').addEventListener('submit', addUser);
document.getElementById('addEntityForm').addEventListener('submit', addEntity);

// Fetch and display users and zoo entities on page load
fetchUsers();
fetchEntities();
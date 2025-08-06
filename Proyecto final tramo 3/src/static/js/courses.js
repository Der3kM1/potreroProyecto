const apiUrl = 'https://potrero-digital-api.vercel.app/courses';

document.addEventListener('DOMContentLoaded', () => {
    fetchCourses();
});

function fetchCourses() {
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            displayCourses(data);
        })
        .catch(error => console.error('Error fetching courses:', error));
}

function displayCourses(courses) {
    const coursesContainer = document.getElementById('courses-container');
    coursesContainer.innerHTML = '';

    courses.forEach(course => {
        const courseCard = document.createElement('div');
        courseCard.className = 'course-card';
        courseCard.innerHTML = `
            <h3 class="course-title">${course.title}</h3>
            <p class="course-description">${course.description}</p>
            <button class="detail-button" onclick="showCourseDetail('${course.id}')">Ver Detalle</button>
        `;
        coursesContainer.appendChild(courseCard);
    });
}

function showCourseDetail(courseId) {
    // redirige a la página de detalle del curso
    window.location.href = `/detail/${courseId}`;
}
// ============================================================
// PROJECTS FILTER AND RENDER
// ============================================================

document.addEventListener('DOMContentLoaded', function() {
    'use strict';

    const projectsGrid = document.getElementById('projectsGrid');
    const filterButtons = document.getElementById('filterButtons');

    let projects = [];
    let currentFilter = 'all';

    // ============================================================
    // FETCH PROJECTS DATA
    // ============================================================
    async function fetchProjects() {
        try {
            const response = await fetch('data/projects.json');
            if (!response.ok) {
                throw new Error('Failed to load projects data');
            }
            const data = await response.json();
            projects = data.projects || [];
            renderProjects(projects);
        } catch (error) {
            console.error('Error loading projects:', error);
            if (projectsGrid) {
                projectsGrid.innerHTML = `
                    <div class="error-message">
                        <p>Unable to load projects. Please try again later.</p>
                    </div>
                `;
            }
        }
    }

    // ============================================================
    // RENDER PROJECTS
    // ============================================================
    function renderProjects(projectsToRender) {
        if (!projectsGrid) return;

        if (projectsToRender.length === 0) {
            projectsGrid.innerHTML = `
                <div class="no-projects">
                    <p>No projects found for the selected filter.</p>
                </div>
            `;
            return;
        }

        projectsGrid.innerHTML = projectsToRender.map(function(project) {
            const metricsHtml = project.metrics ? Object.entries(project.metrics).map(function([key, value]) {
                return `<span><strong>${value}</strong> ${key.replace('_', ' ')}</span>`;
            }).join('') : '';

            const stackHtml = project.stack ? project.stack.map(function(tech) {
                return `<span class="stack-tag">${tech}</span>`;
            }).join('') : '';

            const imagePath = project.image || `assets/images/projects/${project.id}/dashboard.png`;

            return `
                <div class="project-card" data-tags="${(project.tags || []).join(' ')}">
                    <div class="project-image">
                        <img src="${imagePath}" alt="${project.name}" loading="lazy" />
                    </div>
                    <div class="project-body">
                        <h3>${project.name}</h3>
                        <p>${project.description}</p>
                        <div class="project-metrics">
                            ${metricsHtml}
                        </div>
                        <div class="project-stack">
                            ${stackHtml}
                        </div>
                        <div class="project-links">
                            ${project.github ? `<a href="${project.github}" target="_blank" rel="noopener noreferrer" class="btn btn-secondary btn-sm">GitHub</a>` : ''}
                            ${project.demo ? `<a href="${project.demo}" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm">Live Demo</a>` : ''}
                        </div>
                    </div>
                </div>
            `;
        }).join('');
    }

    // ============================================================
    // FILTER PROJECTS
    // ============================================================
    function filterProjects(filter) {
        currentFilter = filter;

        // Update active button
        if (filterButtons) {
            const buttons = filterButtons.querySelectorAll('.filter-btn');
            buttons.forEach(function(btn) {
                btn.classList.remove('active');
                if (btn.dataset.filter === filter) {
                    btn.classList.add('active');
                }
            });
        }

        // Filter projects
        let filteredProjects = projects;
        if (filter !== 'all') {
            filteredProjects = projects.filter(function(project) {
                return (project.tags || []).includes(filter);
            });
        }

        renderProjects(filteredProjects);
    }

    // ============================================================
    // EVENT LISTENERS FOR FILTER BUTTONS
    // ============================================================
    if (filterButtons) {
        filterButtons.addEventListener('click', function(e) {
            const btn = e.target.closest('.filter-btn');
            if (btn) {
                const filter = btn.dataset.filter;
                if (filter) {
                    filterProjects(filter);
                }
            }
        });
    }

    // ============================================================
    // INITIALIZE
    // ============================================================
    fetchProjects();

});
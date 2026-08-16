// ============================================================
// PROJECTS FILTER AND RENDER 
// ============================================================

document.addEventListener('DOMContentLoaded', function() {
    'use strict';

    var projectsGrid = document.getElementById('projectsGrid');
    var filterButtons = document.getElementById('filterButtons');

    var projectsData = [];
    var currentFilter = 'all';

    // ============================================================
    // FETCH PROJECTS DATA
    // ============================================================
    async function fetchProjects() {
        try {
            var response = await fetch('data/projects.json');
            if (!response.ok) {
                throw new Error('Failed to load projects data');
            }
            var data = await response.json();
            projectsData = data.projects || [];
            renderProjects(projectsData);
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
    // RENDER PROJECTS - UPDATED WITH NEW STRUCTURE
    // ============================================================
    function renderProjects(projects) {
        if (!projectsGrid) return;

        if (projects.length === 0) {
            projectsGrid.innerHTML = `
                <div class="no-projects">
                    <p>No projects found for the selected filter.</p>
                </div>
            `;
            return;
        }

        var html = '';

        for (var i = 0; i < projects.length; i++) {
            var project = projects[i];
            var techStackDisplay = project.tech_stack || project.stack.join(' · ');
            var delayClass = 'animate-on-load-delay-' + ((i % 5) + 1);
            var imagePath = project.image || 'assets/images/projects/' + project.id + '/dashboard.png';

            // Build links
            var linksHtml = '';

            if (project.github) {
                linksHtml += '<a href="' + project.github + '" target="_blank" class="btn btn-sm btn-secondary">';
                linksHtml += '<i class="fab fa-github"></i> GitHub';
                linksHtml += '</a>';
            }

            if (project.demo) {
                linksHtml += '<a href="' + project.demo + '" target="_blank" class="btn btn-sm btn-primary">';
                linksHtml += '<i class="fas fa-rocket"></i> Deploy';
                linksHtml += '</a>';
            }

            html += `
                <div class="project-card animate-on-load ${delayClass}" data-tags="${(project.tags || []).join(' ')}">
                    <div class="project-image">
                        <img src="${imagePath}" alt="${project.name}" loading="lazy" />
                    </div>
                    <div class="project-body">
                        <h3>${project.name}</h3>
                        <p class="project-description">${project.description}</p>
                        <div class="project-tech-stack">
                            <span class="tech-label">Tech Stack:</span>
                            <span class="tech-items">${techStackDisplay}</span>
                        </div>
                        <div class="project-results">
                            <span class="results-label">Results</span>
                            ${project.results || ''}
                        </div>
                        <div class="project-links">
                            ${linksHtml}
                        </div>
                    </div>
                </div>
            `;
        }

        projectsGrid.innerHTML = html;

        // Set data-tags for filtering
        var projectCards = document.querySelectorAll('.project-card');
        projectCards.forEach(function(card, index) {
            var project = projects[index];
            if (project && project.tags) {
                card.setAttribute('data-tags', project.tags.join(' '));
            }
        });
    }

    // ============================================================
    // FILTER PROJECTS
    // ============================================================
    function filterProjects(filter) {
        currentFilter = filter;

        // Update active button
        if (filterButtons) {
            var buttons = filterButtons.querySelectorAll('.filter-btn');
            buttons.forEach(function(btn) {
                btn.classList.remove('active');
                if (btn.dataset.filter === filter) {
                    btn.classList.add('active');
                }
            });
        }

        // Filter projects
        var filteredProjects = projectsData;
        if (filter !== 'all') {
            filteredProjects = projectsData.filter(function(project) {
                return (project.tags || []).includes(filter);
            });
        }

        renderProjects(filteredProjects);
    }

    // ============================================================
    // EVENT LISTENERS
    // ============================================================
    if (filterButtons) {
        filterButtons.addEventListener('click', function(e) {
            var btn = e.target.closest('.filter-btn');
            if (btn) {
                var filter = btn.dataset.filter;
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
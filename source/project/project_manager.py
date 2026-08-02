"""
RanZiz AI Project Manager
Version 1.0
"""

from source.project.project import Project


class ProjectManager:

    def __init__(self):

        self.projects = {}

        self.counter = 1

    def create(self, title):

        project_id = f"RZ-{self.counter:06}"

        project = Project(
            project_id,
            title
        )

        self.projects[project_id] = project

        self.counter += 1

        return project

    def get(self, project_id):

        return self.projects.get(project_id)

    def list_projects(self):

        return list(self.projects.values())
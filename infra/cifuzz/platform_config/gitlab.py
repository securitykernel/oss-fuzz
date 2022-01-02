# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Module for getting the configuration CIFuzz needs to run on GitLab."""
import logging
import os

import platform_config


class PlatformConfig(platform_config.BasePlatformConfig):
  """CI environment for GitLab."""

  @property
  def project_src_path(self):
    """Returns the manually checked out path of the project's source if
    specified or the value of CI_PROJECT_DIR if not."""
    return os.getenv('CI_PROJECT_DIR')

  @property
  def workspace(self):
    """Returns the workspace."""
    return os.getenv('CI_PROJECT_DIR')

  @property
  def project_repo_owner(self):
    """Returns the project repo owner (githubism).
    Assuming that top-level group reflects owner's
    name, e.g., gitlab-org is the owner of repo
    gitlab-org/ci-sample-projects/coverage-report."""
    return os.getenv('CI_PROJECT_ROOT_NAMESPACE')

  @property
  def project_repo_name(self):
    """Returns the project repo name."""
    return os.environ.get('CI_PROJECT_NAME')

  @property
  def actor(self):
    """Name of the actor for the CI."""
    return os.environ.get('GITLAB_USER_LOGIN')

  @property
  def token(self):
    """Returns the CI API token."""
    return os.environ.get('CI_JOB_TOKEN')

  @property
  def filestore(self):
    """Returns the filestore used to store persistent data."""
    return os.environ.get('FILESTORE', 'git')

  @property
  def base_commit(self):
    """Returns the previous commit sha for commit-fuzzing"""
    base_commit = None
    if os.getenv('CI_PIPELINE_SOURCE') == 'push':
      base_commit = os.getenv('CI_COMMIT_BEFORE_SHA')
    logging.debug('base_commit: %s.', base_commit)
    return base_commit

  @property
  def base_ref(self):
    """Returns the base commit sha for a merge request"""
    # could also be CI_MERGE_REQUEST_TARGET_BRANCH_NAME
    return os.getenv('CI_MERGE_REQUEST_DIFF_BASE_SHA')
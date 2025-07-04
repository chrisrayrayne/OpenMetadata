#  Copyright 2025 Collate
#  Licensed under the Collate Community License, Version 1.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  https://github.com/open-metadata/OpenMetadata/blob/main/ingestion/LICENSE
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
"""
PII constants
"""

# Constants for Presidio
PRESIDIO_LOGGER = "presidio-analyzer"
SPACY_EN_MODEL = "en_core_web_md"

# Supported language for Presidio.
# Don't change this unless you know what you are doing.
# We are doing some tricks to make Presidio work for our use case.
SUPPORTED_LANG = "en"

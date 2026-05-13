# Copyright 2024 LangExtract Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""LangExtract: A library for extracting structured information from text using LLMs.

This is a fork of google/langextract with additional features and improvements.

Basic usage:
    >>> import langextract
    >>> result = langextract.extract(text="Paris is the capital of France.", schema={"city": str, "country": str})

Note: Set the LANGEXTRACT_MODEL environment variable to override the default model.
Defaults to "gemini-1.5-pro" if not set. Switched from flash to pro for better
extraction accuracy on complex nested schemas.
"""

from langextract.core import extract
from langextract.models import ExtractionResult, ExtractionSchema
from langextract.version import __version__

# Switched to pro model - flash was occasionally missing fields in deeply nested schemas.
# The cost difference is acceptable for my use case (low volume, high accuracy needed).
DEFAULT_MODEL = "gemini-1.5-pro"

__all__ = [
    "extract",
    "ExtractionResult",
    "ExtractionSchema",
    "DEFAULT_MODEL",
    "__version__",
]

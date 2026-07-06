"""Custom exceptions for jsonsubschema.

Originally created on May 11, 2020 by Andrew Habib.
Contains changes by The GHGA Authors.
SPDX-License-Identifier: Apache-2.0
"""

__all__ = [
    "UnsupportedEnumCanonicalization",
    "UnsupportedNegatedArray",
    "UnsupportedNegatedNumeric",
    "UnsupportedNegatedObject",
    "UnsupportedRecursiveRef",
]


class _UnsupportedCase(Exception):
    """Base class for schemas that jsonsubschema cannot handle."""


class _CanonicalizationError(_UnsupportedCase):
    """Raised when a schema cannot be canonicalized."""


class _SubtypeCheckError(_UnsupportedCase):
    """Raised when a subtype check cannot be performed."""


class UnsupportedRecursiveRef(_CanonicalizationError):
    """Raised when a schema uses an unsupported recursive/circular ``$ref``."""

    def __init__(self, schema, which_side):
        self.schema = schema
        self.which_side = which_side

    def __str__(self):
        """Return human-readable error message."""
        return f"Recursive schemas are not supported. {self.which_side} is recursive."


class UnsupportedEnumCanonicalization(_CanonicalizationError):
    """Raised when an enum schema of an unsupported type cannot be canonicalized."""

    def __init__(self, tau, schema):
        self.tau = tau
        self.schema = schema

    def __str__(self):
        """Return human-readable error message."""
        return f"Canonicalizing an enum schema of type {self.tau} is not supported."


class UnsupportedNegatedObject(_SubtypeCheckError):
    """Raised when negating an object schema is not supported."""

    def __init__(self, schema):
        self.schema = schema

    def __str__(self):
        """Return human-readable error message."""
        return f"Object negation at {self.schema} is not supported."


class UnsupportedNegatedNumeric(_SubtypeCheckError):
    """Raised when negating a numeric schema is not supported.

    The complement of an integer schema contains the non-integer numbers,
    and the complement of a ``multipleOf`` constraint contains the
    non-multiples; neither is expressible in the internal checker language.
    """

    def __init__(self, schema):
        self.schema = schema

    def __str__(self):
        """Return human-readable error message."""
        return f"Negation of the numeric schema {self.schema} is not supported."


class UnsupportedNegatedArray(_SubtypeCheckError):
    """Raised when negating an array schema is not supported."""

    def __init__(self, schema):
        self.schema = schema

    def __str__(self):
        """Return human-readable error message."""
        return f"Array negation at {self.schema} is not supported."


# class UnsupportedSchemaType(_Error):
#     '''
#     Probably this is not required since custom types are not
#     supported by jsonschema validation anyways; so we will not reat
#     a case that uses this exception.'''

#     def __init__(self, schema, tau):
#         self.schema = schema
#         self.tau = tau

#     def __str__(self):
#         return '{} is unsupported jsonschema type in schema: {}'.format(
#             self.tau, self.schema)


# class UnsupportedSubtypeChecker(_Error):

#     def __init__(self, schema, desc):
#         self.schema = schema
#         self.desc = desc

#     def __str__(self):
#         return '{} is unsupported. Schema: {}'.format(self.desc, self.schema)

"""
Models for GenNotes Variant and Relation elements.

## About Tags
Most data in GenNotes is stored as key/value tags related to these elements.
Users aren't constrained by database design to particular keys or values, but
for now, I recommend tag keys match this regex format (it may be important for
later optimizing with db indexing and Django): `^[a-z][a-z0-9]*(_[a-z0-9]+)*`.
    -- Madeleine
"""
from django.contrib.postgres.fields import HStoreField
from django.db import models

import reversion


class Variant(models.Model):
    """
    Gennotes Variant element model.

    ## Special Tags
    The following keys are currently special/protected. They're used to find a
    variant based on location and sequence and are indexed in our db to
    optimize searches:
    'chrom_b37', 'pos_b37', 'ref_allele_b37', 'var_allele_b37'
    """
    tags = HStoreField()


class Relation(models.Model):
    """
    Gennotes Relation element model.

    ## Special Tags
    The following key is special/protected; it's used to identify a relation
    and is indexed in our db to optimize searches:
    'type'
    """
    variant = models.ForeignKey(Variant)
    tags = HStoreField()


reversion.register(Variant)
reversion.register(Relation)

<<<<<<< HEAD
-- Dimension table for NYC taxi zones
-- This is a simple pass-through from the seed file, but having it as a model
-- allows for future enhancements (e.g., adding calculated fields, filtering)

select
    locationid as location_id,
    borough,
    zone,
    service_zone
=======
-- Dimension table for NYC taxi zones
-- This is a simple pass-through from the seed file, but having it as a model
-- allows for future enhancements (e.g., adding calculated fields, filtering)

select
    locationid as location_id,
    borough,
    zone,
    service_zone
>>>>>>> a87db69c4b64cd09b9ae6cdc8ac36ab2587a1015
from {{ ref('taxi_zone_lookup') }}
from tap_kit.streams import Stream
import singer

LOGGER = singer.get_logger()


class ScoreStream(Stream):

    stream = 'score'

    meta_fields = dict(
        key_properties=['snapped_lat'],
        api_path='/score',
        replication_method='full',
        selected_by_default=False

    )

    schema = {
        "properties": {
            "status": {
                "type": ["null", "string"]
            },
            "walkscore": {
                "type": ["null", "string"]
            },
            "description": {
                "type": ["null", "string"]
            },
            "updated": {
                "type": ["null", "string"]
            },
            "logo_url": {
                "type": ["null", "string"]
            },
            "more_info_icon": {
                "type": ["null", "string"]
            },
            "more_info_link": {
                "type": ["null", "string"]
            },
            "ws_link": {
                "type": ["null", "string"]
            },
            "help_link": {
                "type": ["null", "string"]
            },
            "snapped_lat": {
                "type": ["null", "string"]
            },
            "snapped_lon": {
                "type": ["null", "string"]
            },
            "transit": {
                "type": ["null", "json"]
            },
            "bike": {
                "type": ["null", "json"]
            },
        },
    }


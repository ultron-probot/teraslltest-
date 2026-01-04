try:
    from bson.codec_options import CodecOptions, DEFAULT_CODEC_OPTIONS
    print("Successfully imported CodecOptions and DEFAULT_CODEC_OPTIONS")
except ImportError as e:
    print(f"Import error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

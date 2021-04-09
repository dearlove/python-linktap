import asyncio

import linktap


async def main():
    username = "example_username"
    apiKey = "example_apiKey"
    lt = linktap.LinkTap(username, apiKey)
    all_devices = lt.get_all_devices()
    if all_devices == "error":
        print("all_devices - error")
        LOGGER.info(
            "get_link_tap_devices: The minimum interval of calling this API is 5 minutes."
        )
        data = None
        ready = False
        return False
    elif all_devices is None:
        print("all_devices - none")
        LOGGER.info("Get all devices failed")
        data = None
        ready = False
        return False
    else:
        print("no error detected")
        data = all_devices
        print(data)
        ready = True
        return True


if __name__ == "__main__":
    print("Starting main")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

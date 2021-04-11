#!/usr/bin/env python3

import sys
import requests


class LinkTap:
    def __init__(self, username, apiKey):
        self.base_url = "https://www.link-tap.com/api/"
        self.username = username
        self.apiKey = apiKey

    def call_api(self, url, payload):
        try:
            r = requests.post(url, data=payload)
            if r.status_code == requests.codes.ok:
                data = r.json()
                if data["result"] == "error":
                    return "error"
                elif data is None:
                    return "error"
                else:
                    return data
            else:
                return "error"
        except requests.exceptions.RequestException:
            LOGGER.info("Request failed: RequestException")
            pass
        except socket.gaierror:
            LOGGER.info("Request failed: gaierror Name does not resolve")
            pass
        except urllib3.exceptions.NewConnectionError:
            LOGGER.info("Request failed: NewConnectionError")
            pass
        except urllib3.exceptions.MaxRetryError:
            LOGGER.info("Request failed: MaxRetryError")
            pass
        except requests.exceptions.ConnectionError:
            LOGGER.info("Request failed: ConnectionError")
            pass

    def activate_instant_mode(self, gatewayId, taplinkerId, action, duration, eco):
        url = self.base_url + "activateInstantMode"

        # autoBack:  Re-activate watering plan after Instant Mode
        auto_back = "true"

        if action:
            action = "true"
        else:
            action = "false"

        if eco:
            eco = "true"
        else:
            eco = "false"

        payload = {
            "username": self.username,
            "apiKey": self.apiKey,
            "gatewayId": gatewayId,
            "taplinkerId": taplinkerId,
            "action": action,
            "duration": duration,
            "eco": eco,
            "autoBack": auto_back,
        }
        ret = self.call_api(url, payload)
        return ret

    def activate_interval_mode(self, gatewayId, taplinkerId):
        url = self.base_url + "activateIntervalMode"

        payload = {
            "username": self.username,
            "apiKey": self.apiKey,
            "gatewayId": gatewayId,
            "taplinkerId": taplinkerId,
        }
        ret = self.call_api(url, payload)
        return ret

    def activate_odd_even_mode(self, gatewayId, taplinkerId):
        url = self.base_url + "activateOddEvenMode"

        payload = {
            "username": self.username,
            "apiKey": self.apiKey,
            "gatewayId": gatewayId,
            "taplinkerId": taplinkerId,
        }
        ret = self.call_api(url, payload)
        return ret

    def activate_seven_day_mode(self, gatewayId, taplinkerId):
        url = self.base_url + "activateSevenDayMode"

        payload = {
            "username": self.username,
            "apiKey": self.apiKey,
            "gatewayId": gatewayId,
            "taplinkerId": taplinkerId,
        }
        ret = self.call_api(url, payload)
        return ret

    def activate_month_mode(self, gatewayId, taplinkerId):
        url = self.base_url + "activateMonthMode"

        payload = {
            "username": self.username,
            "apiKey": self.apiKey,
            "gatewayId": gatewayId,
            "taplinkerId": taplinkerId,
        }
        ret = self.call_api(url, payload)
        return ret

    def get_all_devices(self):
        url = self.base_url + "getAllDevices"
        payload = {"username": self.username, "apiKey": self.apiKey}
        ret = self.call_api(url, payload)
        return ret

    def get_watering_status(self, taplinkerId):
        url = self.base_url + "getWateringStatus"
        payload = {
            "username": self.username,
            "apiKey": self.apiKey,
            "taplinkerId": taplinkerId,
        }
        ret = self.call_api(url, payload)
        return ret


if __name__ == "__main__":
    # Return output from get_all_devices
    try:
        import sys

        if len(sys.argv) < 3 or len(sys.argv) > 3:
            print(
                """\
                When called as a python program this script will
                return all device information from the LinkTap API.

                Usage:  python linktap.py <username> <apiKey>
                """
            )
            sys.exit(0)

        lt = LinkTap(sys.argv[1], sys.argv[2])
        all_devices = lt.get_all_devices()
        if all_devices == "error":
            print(
                "Get all devices failed - API error - minimum interval of calling this API is 5 minutes."
            )
            LOGGER.info(
                "get_link_tap_devices: The minimum interval of calling this API is 5 minutes."
            )
            data = None
            sys.exit(1)
        elif all_devices is None:
            print("Get all devices failed - no values returned.")
            LOGGER.info("Get all devices failed")
            data = None
            sys.exit(1)
        else:
            # print("no error detected")
            data = all_devices
            print(data)
            sys.exit(0)

    except (KeyboardInterrupt, SystemExit):
        sys.exit(0)

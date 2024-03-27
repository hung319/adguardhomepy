from adguardhome import AdGuardHome

import asyncio


async def main():
    """Show example how to get status of your AdGuard Home instance."""
    async with AdGuardHome("0.0.0.0") as adguard:
        version = await adguard.version()
        print("AdGuard version:", version)

        active = await adguard.protection_enabled()
        active = "Yes" if active else "No"
        print("Protection enabled?", active)

        if not active:
            print("AdGuard Home protection disabled. Enabling...")
            await adguard.enable_protection()


if __name__ == "__main__":
    asyncio.run(main())

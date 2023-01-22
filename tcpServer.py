import asyncio
from aiorun import run


async def handle_client(reader, writer):
    img = b""
    while True:
        try:
            data = await reader.read(1024 * 1024 * 10)
            if b"EOFEOFEOF" in data:
                data = data.split(b"EOFEOFEOF")
                img += data[0]
                print(len(img))
                img = data[1]
            else:
                img += data
        except Exception:
            break


async def main():
    srv = await asyncio.start_server(handle_client, "0.0.0.0", 55554)
    async with srv:
        await srv.serve_forever()


if __name__ == "__main__":
    run(main())

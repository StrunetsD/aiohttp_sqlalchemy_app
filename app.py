from aiohttp import web
from sqlalchemy.future import select
from db import init_db, get_db
from models import Book

app = web.Application()

async def get_books(request):
    async for session in get_db():
        result = await session.execute(select(Book))
        books = result.scalars().all()
        return web.json_response([book.__dict__ for book in books])

async def get_book(request):
    book_id = int(request.match_info['id'])
    async for session in get_db():
        result = await session.execute(select(Book).filter(Book.id == book_id))
        book = result.scalar_one_or_none()
        if book:
            return web.json_response(book.__dict__)
        return web.HTTPNotFound()

async def create_book(request):
    data = await request.json()
    new_book = Book(**data)
    async for session in get_db():
        session.add(new_book)
        await session.commit()
        return web.json_response(new_book.__dict__, status=201)

async def update_book(request):
    book_id = int(request.match_info['id'])
    data = await request.json()
    async for session in get_db():
        result = await session.execute(select(Book).filter(Book.id == book_id))
        book = result.scalar_one_or_none()
        if book:
            for key, value in data.items():
                setattr(book, key, value)
            await session.commit()
            return web.json_response(book.__dict__)
        return web.HTTPNotFound()

async def delete_book(request):
    book_id = int(request.match_info['id'])
    async for session in get_db():
        result = await session.execute(select(Book).filter(Book.id == book_id))
        book = result.scalar_one_or_none()
        if book:
            await session.delete(book)
            await session.commit()
            return web.Response(status=204)
        return web.HTTPNotFound()

app.router.add_get('/api/books', get_books)
app.router.add_get('/api/books/{id}', get_book)
app.router.add_post('/api/books', create_book)
app.router.add_put('/api/books/{id}', update_book)
app.router.add_delete('/api/books/{id}', delete_book)

async def init_app():
    await init_db()

if __name__ == '__main__':
    app.on_startup.append(init_app)
    web.run_app(app, host='127.0.0.1', port=8080)
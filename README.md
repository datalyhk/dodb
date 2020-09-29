# DO Db

## Setup

- Create `dj_secret.key` with Django secret key in `/backend` directory
- Build with `docker-compose up --build`
- Run bash shell `docker-compose exec backend /bin/bash`

### In backend shell:

- Initial migrate `python3 manage.py migrate`
- Create superuser `python3 manage.py createsuperuser`
- Import scraped drug list using `python3 manage.py importcsv *filename*`
- E.g. `python3 manage.py importcsv druglist_sample.csv`

### REST API endpoints

- `/api/products/`
- `/api/products/<product_id>/`
- `/api/companies/`
- `/api/companies/<company_id>/`
- `/api/ingredients/`
- `/api/ingredients/<ingredient_id>/`


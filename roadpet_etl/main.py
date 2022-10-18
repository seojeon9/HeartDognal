import sys
from datajob.datamart.actor_datamart import Actor
from datajob.datamart.company_datamart import Company
from datajob.datamart.genre_datamart import Genre
from datajob.datamart.movie_audi_datamart import MovieAudi
from datajob.datamart.movie_datamart import Movie
from datajob.datamart.movie_hit_datamart import MovieHit
from datajob.datamart.movie_rank_datamart import MovieRank
from datajob.datamart.movie_sales_datamart import MovieSales
from datajob.datamart.movie_score_datamart import MovieScore
from datajob.datamart.movie_scrn_datamart import MovieScrn
from datajob.datamart.movie_search_datamart import MovieSearch
from datajob.datamart.movie_show_datamart import MovieShow
from datajob.etl.extract.daily_boxoffice_api import DailyBoxofficeExtractor
from datajob.etl.extract.movie_detail import MovieDetailApiExtractor
from datajob.etl.extract.movie_score import MovieScoreExtractor
from datajob.etl.extract.naver_datalab_api import NaverDatalabApiExtractor
from datajob.etl.extract.naver_search_api import NaverSearchMovieExtractor
from datajob.etl.transform.daily_boxoffice_transform import DailyBoxOfficeTransformer
from datajob.etl.transform.movie_detail_transform import MovieDetailTransformer
from datajob.etl.transform.movie_score_transform import MovieScoreTransformer
from datajob.etl.transform.movie_url_and_actors_transform import MovieUrlAndActorsTransformer
from datajob.etl.transform.naver_datalab_transform import NaverDatalabTransformer

def extract_execute():
    NaverDatalabApiExtractor.extract_data()
    NaverSearchMovieExtractor.extract_data()


def transform_execute():
    MovieUrlAndActorsTransformer.transform()
    NaverDatalabTransformer.transform()


def datamart_execute():
    Actor.save()
    Company.save()
    Genre.save()
    MovieAudi.save()
    MovieRank.save()
    MovieSales.save()
    MovieScore.save()
    MovieScrn.save()
    MovieSearch.save()
    MovieShow.save()


works = {
    'extract':{
        'execute':extract_execute,
        'daily_boxoffice': DailyBoxofficeExtractor.extract_data,
        'movie_detail':MovieDetailApiExtractor.extract_data,
        'movie_score':MovieScoreExtractor.extract_data,
        'naver_datalab':NaverDatalabApiExtractor.extract_data,
        'naver_search':NaverSearchMovieExtractor.extract_data
    },
    'transform':{
        'daily_boxoffice':DailyBoxOfficeTransformer.transform,
        'movie_detail':MovieDetailTransformer.transform,
        'movie_score':MovieScoreTransformer.transform,
        'movie_url_actor':MovieUrlAndActorsTransformer.transform,
        'naver_datalab':NaverDatalabTransformer.transform,
        'execute':transform_execute
    },
    'datamart':{
        'execute':datamart_execute,
        'movie_hit':MovieHit.save,
        'movie':Movie.save,
        'actor':Actor.save,
        'company':Company.save,
        'genre':Genre.save,
        'movieAudi':MovieAudi.save,
        'movieRank':MovieRank.save,
        'movieSales':MovieSales.save,
        'movieScore':MovieScore.save,
        'movieScrn':MovieScrn.save,
        'movieSearch':MovieSearch.save,
        'movieShow':MovieShow.save
        }

}

if __name__ == "__main__":
    args = sys.argv
    print(args)

    # main.py 작업(extract, transform, datamart) 저장할 위치(테이블)
    # 매개변수 2개
    if len(args) != 3:
        raise Exception('2개의 전달인자가 필요합니다.')

    if args[1] not in works.keys():
        raise Exception('첫번째 전달인자가 이상함 >> ' + str(works.keys()))

    if args[2] not in works[args[1]].keys():
        raise Exception('두번째 전달인자가 이상함 >> ' + str(works[args[1]].keys()))

    work = works[args[1]][args[2]]
    work()

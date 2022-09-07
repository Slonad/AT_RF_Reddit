*** Settings ***
Resource          suite.resource
Force Tags        api:online

*** Variables ***
${SUBREDDIT_NAME_ONE}=  technology
${SUBREDDIT_NAME_TWO}=  dadjokes
${THREAD_FULLNAME}=     t3_x7ztyf
${QUERY}=       Inside some
${MESSAGE}=     Some message
${TITLE}=       Some post

*** Test Cases ***
Test Search Thread Comment Delete Comment by Title
    [Documentation]    Поиск треда по заголовку. комментирование и удаление коммента
    [Tags]    check:positive    main_test_word

    ${response}=    SubredditsApi.search_thread     subreddit_name=${SUBREDDIT_NAME_ONE}
                    ...                             query=${QUERY}
    Should be equal     ${response.status_code}     ${200}

    ${thread_fullname}=     Tools.get_not_archived_thread   ${response}
    ${response}=    LinksCommentsApi.post_comment   thread_id=${thread_fullname}
                    ...                             message=${MESSAGE}
    Should be equal     ${response.status_code}     ${200}

    ${reddit_fullname}=     Set Variable     ${response.json()['jquery'][18][3][0][0]['data']['name']}
    ${response}=    LinksCommentsApi.delete_t_entity     reddit_fullname=${reddit_fullname}
    Should be equal     ${response.status_code}     ${200}

Test Search Thread Comment Delete Comment by Key
    [Documentation]    Поиск треда по ключу. комментирование и удаление коммента
    [Tags]    check:positive    main_test_key

    ${response}=    LinksCommentsApi.post_comment   thread_id=${THREAD_FULLNAME}
                    ...                             message=${MESSAGE}
    Should be equal     ${response.status_code}     ${200}

    ${reddit_fullname}=     Set Variable    ${response.json()['jquery'][18][3][0][0]['data']['name']}
    ${response}=    LinksCommentsApi.delete_t_entity     reddit_fullname=${reddit_fullname}
    Should be equal     ${response.status_code}     ${200}

Test Subscribe and Post
    [Documentation]    Подписка на сабреддит и создание пустого поста
    [Tags]    check:positive    main_test_post
    [Teardown]      Run Keywords    SubredditsApi.subscribe_subreddit   subreddit_name=${SUBREDDIT_NAME_TWO}
                                    ...                                 sub=unsub
                    ...     AND     Delete Post     ${response}

    ${response}=    SubredditsApi.subscribe_subreddit   subreddit_name=${SUBREDDIT_NAME_TWO}
                    ...                                 sub=sub
    Should be equal     ${response.status_code}     ${200}

    ${response}=    SubredditsApi.make_post     subreddit_name=${SUBREDDIT_NAME_TWO}
                    ...                         title=${TITLE}
                    ...                         text=${MESSAGE}
    Should be equal     ${response.status_code}     ${200}

*** Keywords ***
Delete Post
    [Arguments]    ${response}

    ${fullname_post}=   Tools.get_fullname_post     response=${response}
    ${response}=    LinksCommentsApi.delete_t_entity    reddit_fullname=${fullname_post}
    Should be equal     ${response.status_code}     ${200}

*** Settings ***
Resource          suite.resource
Force Tags        api:online

*** Test Cases ***
Test Get Info Current User
    [Documentation]    Проверка получения информации о клиенте
    [Tags]    check:positive
    ${response}=    AccountApi.get_info_current_user
    Should be equal     ${response.status_code}     ${200}

Test Get Empty Friendlist Current User
    [Documentation]    Проверка получения пустого списка друзей клиента
    [Tags]    check:positive
    ${response}=    AccountApi.get_friend_list_current_user
    Should be equal     ${response.status_code}     ${200}
    Validate.empty_friend_list_current_user     ${response.json()}

Test Get Karma Current User
    [Documentation]    Проверка получения баланса кармы клиента
    [Tags]    check:positive
    ${response}=    AccountApi.get_karma_current_user
    Should be equal     ${response.status_code}     ${200}
    Validate.karma_current_user     ${response.json()}


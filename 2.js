let data =
    '{"name":"New Playlist","description":"New playlist description","public":false}';
let ACCESS_TOKEN =
    "BQAmgnfDoalQkyGIEsfGofjONQIu91NWunHEZEoNy9K-vuVP938w_VWcHL__KVuB4AHhrgurXW9oxw77gafxxuyftPD5UYF8sBxW0pp1i8eRDi6one_iq72IUwyUsbdsJut7yVl4djOrybf9n2mYOrkz-qqf8UvGq6wYGmn3nuyqUy8gfX_3F9h1YE5fwIf216tKa3AOsg7b9RDOXALa9GG1n_s2";

const func = async() => {
    const ret = await fetch("https://api.spotify.com/v1/users/shivam/playlists", {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
            "Content-type": "application/json; charset=UTF-8",
            Accept: "application/json",
            Authorization: `Bearer ${ACCESS_TOKEN}`,
        },
    });

    console.log(ret);
};
func();
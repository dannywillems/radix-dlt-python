NODE_FINDER = ("https://alphanet.radixdlt.com/node-finder", 443)

RAW = {
    "creator": {
        "serializer": "BASE64",
        "value": "ArnzOG3RWxxoie6PHilzP8CuLGJsZlrQdizq0yFHgLoK"
    },
    "description": "The Radix test Universe",
    "genesis": [
        {
            "action": "STORE",
            "classification": "commodity",
            "description": "Radix POW",
            "destinations": [
                {
                    "serializer": "EUID",
                    "value": "4805250210156151332276828698"
                }
            ],
            "icon": {
                "serializer": "BASE64",
                "value": "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\u003d"
            },
            "id": {
                "serializer": "EUID",
                "value": "79416"
            },
            "iso": "POW",
            "label": "Proof of Work",
            "maximum_units": 0,
            "owners": [
                {
                    "public": {
                        "serializer": "BASE64",
                        "value": "ArnzOG3RWxxoie6PHilzP8CuLGJsZlrQdizq0yFHgLoK"
                    },
                    "serializer": 547221307,
                    "version": 100
                }
            ],
            "serializer": 62583504,
            "settings": 4096,
            "signatures": {
                "4805250210156151332276828698": {
                    "r": {
                        "serializer": "BASE64",
                        "value": "b8Wk8SauLmpkaFmfOJuS8unAT3Lzv4GVH0GmeVCEpJ4\u003d"
                    },
                    "s": {
                        "serializer": "BASE64",
                        "value": "ANeCu2E2fTlXNKtj6leYhPBNmMuR9OpeAHJ8+Rrd5FeT"
                    },
                    "serializer": -434788200,
                    "version": 100
                }
            },
            "sub_units": 0,
            "timestamps": {
                "default": 1488326400000,
                "expires": 9223372036854775807
            },
            "type": "COMMODITY",
            "version": 100
        },
        {
            "action": "STORE",
            "classification": "currencies",
            "description": "Radix Test currency asset",
            "destinations": [
                {
                    "serializer": "EUID",
                    "value": "4805250210156151332276828698"
                }
            ],
            "icon": {
                "serializer": "BASE64",
                "value": "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\u003d"
            },
            "id": {
                "serializer": "EUID",
                "value": "2571410"
            },
            "iso": "TEST",
            "label": "Test Rads",
            "maximum_units": 0,
            "owners": [
                {
                    "public": {
                        "serializer": "BASE64",
                        "value": "ArnzOG3RWxxoie6PHilzP8CuLGJsZlrQdizq0yFHgLoK"
                    },
                    "serializer": 547221307,
                    "version": 100
                }
            ],
            "scrypt": {
                "serializer": 549088296,
                "version": 100
            },
            "serializer": 62583504,
            "settings": 20483,
            "signatures": {
                "4805250210156151332276828698": {
                    "r": {
                        "serializer": "BASE64",
                        "value": "fAlFvF1YS6aNoYOAHoFDurjPmpSiZtzUHK2/32e2GYI\u003d"
                    },
                    "s": {
                        "serializer": "BASE64",
                        "value": "AMhNKocrcrfqUtK0lV6neFGAo8Ei14SUw8odFdLI1j4X"
                    },
                    "serializer": -434788200,
                    "version": 100
                }
            },
            "sub_units": 100000,
            "timestamps": {
                "default": 1488326400000,
                "expires": 9223372036854775807
            },
            "type": "CURRENCY",
            "version": 100
        },
        {
            "action": "STORE",
            "destinations": [
                {
                    "serializer": "EUID",
                    "value": "4805250210156151332276828698"
                }
            ],
            "encrypted": {
                "serializer": "BASE64",
                "value": "BQAAAa4HbWVzc2FnZQMAAAAVUmFkaXguLi4uSnVzdCBJbWFnaW5lDHBhcnRpY2lwYW50cwYAAAFNBQAAAIoHYWRkcmVzcwUAAABAB2FkZHJlc3MDAAAABlNZU1RFTQpzZXJpYWxpemVyAgAAAAj/////5mMn1Ad2ZXJzaW9uAgAAAAgAAAAAAAAAZApzZXJpYWxpemVyAgAAAAj/////rhGDEwR0eXBlAwAAAAZTRU5ERVIHdmVyc2lvbgIAAAAIAAAAAAAAAGQFAAAAuQdhZGRyZXNzBQAAAG0HYWRkcmVzcwMAAAAzMTZKUENWQ3p6REw5bjhXeEtSeGQzR3hrcXlXS0pHcFJwdm8xZlo2eFFjekd6dG56S1NxCnNlcmlhbGl6ZXICAAAACP/////mYyfUB3ZlcnNpb24CAAAACAAAAAAAAABkCnNlcmlhbGl6ZXICAAAACP////+uEYMTBHR5cGUDAAAACFJFQ0VJVkVSB3ZlcnNpb24CAAAACAAAAAAAAABkCnNlcmlhbGl6ZXICAAAACAAAAAAe/f+nB3ZlcnNpb24CAAAACAAAAAAAAABk"
            },
            "operation": "TRANSFER",
            "particles": [
                {
                    "asset_id": {
                        "serializer": "EUID",
                        "value": "2571410"
                    },
                    "destinations": [
                        {
                            "serializer": "EUID",
                            "value": "4805250210156151332276828698"
                        }
                    ],
                    "nonce": 263153973592936,
                    "owners": [
                        {
                            "public": {
                                "serializer": "BASE64",
                                "value": "ArnzOG3RWxxoie6PHilzP8CuLGJsZlrQdizq0yFHgLoK"
                            },
                            "serializer": 547221307,
                            "version": 100
                        }
                    ],
                    "quantity": 100000000000000,
                    "serializer": 1782261127,
                    "version": 100
                }
            ],
            "serializer": -760130,
            "signatures": {
                "4805250210156151332276828698": {
                    "r": {
                        "serializer": "BASE64",
                        "value": "Pixa87IInUKUGixJ8Pm89d2y2QjP2Px5zsHj9/k96Cw\u003d"
                    },
                    "s": {
                        "serializer": "BASE64",
                        "value": "AKjX0RUA471Ns3TRHII8hUs1fuQgIHMRXC1arff8kH3r"
                    },
                    "serializer": -434788200,
                    "version": 100
                }
            },
            "temporal_proof": {
                "atom_id": {
                    "serializer": "EUID",
                    "value": "10667573371185321423197757020"
                },
                "serializer": 1905172290,
                "version": 100,
                "vertices": [
                    {
                        "clock": 0,
                        "commitment": {
                            "serializer": "HASH",
                            "value": "0000000000000000000000000000000000000000000000000000000000000000"
                        },
                        "owner": {
                            "public": {
                                "serializer": "BASE64",
                                "value": "Amd3k/89SAeXolfxtF9BLPCf2t78Wy82q9i8M9xwcaDv"
                            },
                            "serializer": 547221307,
                            "version": 100
                        },
                        "previous": {
                            "serializer": "EUID",
                            "value": "0"
                        },
                        "serializer": -909337786,
                        "signature": {
                            "r": {
                                "serializer": "BASE64",
                                "value": "AKQrtclznyfCHog48Y3pIc3uJVrf6W8DZmY/HvlpqqWd"
                            },
                            "s": {
                                "serializer": "BASE64",
                                "value": "AIuFAAOV0/EGvw3vq3qcdqg0Z/sGQ5A9sqHxHkgrlk+U"
                            },
                            "serializer": -434788200,
                            "version": 100
                        },
                        "timestamps": {
                            "default": 1529343443332
                        },
                        "version": 100
                    }
                ]
            },
            "timestamps": {
                "default": 1488326400000
            },
            "version": 100
        }
    ],
    "magic": 281411585,
    "name": "Radix Testnet",
    "port": 20000,
    "serializer": 492321349,
    "signature.r": {
        "serializer": "BASE64",
        "value": "AKPiVkNpfMgC7qRE6/tm4wk+1fPCuqgYHa/PL1M2MaYr"
    },
    "signature.s": {
        "serializer": "BASE64",
        "value": "AICUs3o06h3XzFJGdXXNRyx6He7+kBfbVY1w/cvXGLJb"
    },
    "timestamp": 1488326400000,
    "type": 1,
    "version": 100
}

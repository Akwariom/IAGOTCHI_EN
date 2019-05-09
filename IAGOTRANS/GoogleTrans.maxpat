{
	"patcher" : 	{
		"fileversion" : 1,
		"appversion" : 		{
			"major" : 8,
			"minor" : 0,
			"revision" : 4,
			"architecture" : "x64",
			"modernui" : 1
		}
,
		"classnamespace" : "box",
		"rect" : [ 707.0, 218.0, 640.0, 480.0 ],
		"bglocked" : 0,
		"openinpresentation" : 0,
		"default_fontsize" : 12.0,
		"default_fontface" : 0,
		"default_fontname" : "Arial",
		"gridonopen" : 1,
		"gridsize" : [ 15.0, 15.0 ],
		"gridsnaponopen" : 1,
		"objectsnaponopen" : 1,
		"statusbarvisible" : 2,
		"toolbarvisible" : 1,
		"lefttoolbarpinned" : 0,
		"toptoolbarpinned" : 0,
		"righttoolbarpinned" : 0,
		"bottomtoolbarpinned" : 0,
		"toolbars_unpinned_last_save" : 0,
		"tallnewobj" : 0,
		"boxanimatetime" : 200,
		"enablehscroll" : 1,
		"enablevscroll" : 1,
		"devicewidth" : 0.0,
		"description" : "",
		"digest" : "",
		"tags" : "",
		"style" : "",
		"subpatcher_template" : "",
		"boxes" : [ 			{
				"box" : 				{
					"id" : "obj-38",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 347.0, 71.0, 88.0, 22.0 ],
					"text" : "Я не понимаю"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-36",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 219.0, 71.0, 120.0, 22.0 ],
					"text" : "je ne comprends pas"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-35",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 313.0, 165.5, 55.0, 22.0 ],
					"text" : "zl slice 2"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-27",
					"items" : [ "afrikaans", "-", "af", ",", "albanian", "-", "sq", ",", "amharic", "-", "am", ",", "arabic", "-", "ar", ",", "armenian", "-", "hy", ",", "azerbaijani", "-", "az", ",", "basque", "-", "eu", ",", "belarusian", "-", "be", ",", "bengali", "-", "bn", ",", "bosnian", "-", "bs", ",", "bulgarian", "-", "bg", ",", "catalan", "-", "ca", ",", "cebuano", "-", "ceb", ",", "chichewa", "-", "ny", ",", "chinese", "-", "zh-cn", ",", "chinese", "-", "zh-tw", ",", "corsican", "-", "co", ",", "croatian", "-", "hr", ",", "czech", "-", "cs", ",", "danish", "-", "da", ",", "dutch", "-", "nl", ",", "english", "-", "en", ",", "esperanto", "-", "eo", ",", "estonian", "-", "et", ",", "filipino", "-", "tl", ",", "finnish", "-", "fi", ",", "french", "-", "fr", ",", "frisian", "-", "fy", ",", "galician", "-", "gl", ",", "georgian", "-", "ka", ",", "german", "-", "de", ",", "greek", "-", "el", ",", "gujarati", "-", "gu", ",", "haitian", "-", "ht", ",", "hausa", "-", "ha", ",", "hawaiian", "-", "haw", ",", "hebrew", "-", "iw", ",", "hindi", "-", "hi", ",", "hmong", "-", "hmn", ",", "hungarian", "-", "hu", ",", "icelandic", "-", "is", ",", "igbo", "-", "ig", ",", "indonesian", "-", "id", ",", "irish", "-", "ga", ",", "italian", "-", "it", ",", "japanese", "-", "ja", ",", "javanese", "-", "jw", ",", "kannada", "-", "kn", ",", "kazakh", "-", "kk", ",", "khmer", "-", "km", ",", "korean", "-", "ko", ",", "kurdish", "-", "ku", ",", "kyrgyz", "-", "ky", ",", "lao", "-", "lo", ",", "latin", "-", "la", ",", "latvian", "-", "lv", ",", "lithuanian", "-", "lt", ",", "luxembourgish", "-", "lb", ",", "macedonian", "-", "mk", ",", "malagasy", "-", "mg", ",", "malay", "-", "ms", ",", "malayalam", "-", "ml", ",", "maltese", "-", "mt", ",", "maori", "-", "mi", ",", "marathi", "-", "mr", ",", "mongolian", "-", "mn", ",", "myanmar", "-", "my", ",", "nepali", "-", "ne", ",", "norwegian", "-", "no", ",", "pashto", "-", "ps", ",", "persian", "-", "fa", ",", "polish", "-", "pl", ",", "portuguese", "-", "pt", ",", "punjabi", "-", "pa", ",", "romanian", "-", "ro", ",", "russian", "-", "ru", ",", "samoan", "-", "sm", ",", "scots", "-", "gd", ",", "serbian", "-", "sr", ",", "sesotho", "-", "st", ",", "shona", "-", "sn", ",", "sindhi", "-", "sd", ",", "sinhala", "-", "si", ",", "slovak", "-", "sk", ",", "slovenian", "-", "sl", ",", "somali", "-", "so", ",", "spanish", "-", "es", ",", "sundanese", "-", "su", ",", "swahili", "-", "sw", ",", "swedish", "-", "sv", ",", "tajik", "-", "tg", ",", "tamil", "-", "ta", ",", "telugu", "-", "te", ",", "thai", "-", "th", ",", "turkish", "-", "tr", ",", "ukrainian", "-", "uk", ",", "urdu", "-", "ur", ",", "uzbek", "-", "uz", ",", "vietnamese", "-", "vi", ",", "welsh", "-", "cy", ",", "xhosa", "-", "xh", ",", "yiddish", "-", "yi", ",", "yoruba", "-", "yo", ",", "zulu", "-", "zu", ",", "Filipino", "-", "fil", ",", "Hebrew", "-", "he" ],
					"maxclass" : "umenu",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "int", "", "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 246.0, 133.5, 153.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-2",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 74.0, 273.0, 32.0, 22.0 ],
					"text" : "print"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-12",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 219.0, 37.0, 216.0, 22.0 ],
					"text" : "ich bin nicht der offiziellen kirchenjesus"
				}

			}
, 			{
				"box" : 				{
					"dontreplace" : 1,
					"id" : "obj-6",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 40.0, 309.0, 544.0, 22.0 ],
					"text" : "\"Ech sinn net hongereg\""
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-3",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 74.0, 41.0, 84.0, 22.0 ],
					"text" : "I'm not hungry"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-8",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 349.0, 197.0, 82.0, 22.0 ],
					"text" : "prepend /dest"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-4",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 74.0, 88.75, 105.0, 22.0 ],
					"text" : "prepend /translate"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-10",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 74.0, 234.0, 102.0, 22.0 ],
					"text" : "OSC-route /result"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-11",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 74.0, 199.0, 97.0, 22.0 ],
					"text" : "udpreceive 7861"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-13",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 74.0, 169.0, 135.0, 22.0 ],
					"text" : "udpsend localhost 7860"
				}

			}
 ],
		"lines" : [ 			{
				"patchline" : 				{
					"destination" : [ "obj-2", 0 ],
					"order" : 1,
					"source" : [ "obj-10", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-6", 1 ],
					"order" : 0,
					"source" : [ "obj-10", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-10", 0 ],
					"source" : [ "obj-11", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-4", 0 ],
					"source" : [ "obj-12", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 0 ],
					"source" : [ "obj-27", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-4", 0 ],
					"source" : [ "obj-3", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-8", 0 ],
					"source" : [ "obj-35", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-4", 0 ],
					"source" : [ "obj-36", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-4", 0 ],
					"source" : [ "obj-38", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-13", 0 ],
					"source" : [ "obj-4", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-13", 0 ],
					"midpoints" : [ 358.5, 231.0, 234.75, 231.0, 234.75, 158.0, 83.5, 158.0 ],
					"source" : [ "obj-8", 0 ]
				}

			}
 ],
		"dependency_cache" : [ 			{
				"name" : "OSC-route.mxo",
				"type" : "iLaX"
			}
 ],
		"autosave" : 0
	}

}

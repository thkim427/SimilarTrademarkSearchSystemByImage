class Distance:
    def __init__(self):
        self.top8 = 8
        self.distance_top = [1, 2, 3, 4, 5, 6, 7, 8]
        self.distance_avg = 10.73
        self.distance_max = 32
        self.distance_min = 7
        self.count_almost_same = 72
        self.count_similar = 3270
        self.count_total = 2039400
        self.distance_top = [1, 2, 3, 4, 5, 6, 7, 8]
        self.distance_similar_b = [3, 4, 5, 6, 7, 8, 9, 10]
        self.distance_total = [
                [0.2, 0.5, 0.8, 6, 7, 14.5, 15],
                [0.2, 1, 11.8, 14, 12.4, 1, 0.2]
            ]
        self.distance_same = [
                [0, 2, 3.5, 4, 8, 3, 4, 6, 2, 6],
                [0, 6, 5.5, 3, 3, 11, 7, 4, 7, 9]
            ]
        self.distance_similar = [
                [0, 2, 3.5, 4, 8, 3, 4, 6, 2, 6, 4.7, 3, 5],
                [0, 6, 5.5, 3, 3, 11, 7, 4, 7, 9, 10, 12, 13]
            ]

    def set_graph(self):
        data = a.results.to_dataframe()
        self.top8 = data.head(n=8).distance.mean()
        self.distance_avg = data['distance'].mean()
        self.distance_max = data['distance'][len(data) - 1]
        self.distance_min = data['distance'][0]
        self.count_total = len(data)
        self.count_almost_same = data.loc[data['distance'] < (self.distance_min+((self.distance_max-self.distance_min)/739))].distance.count()
        self.count_similar = data.loc[data['distance'] < (self.distance_min+((self.distance_max-self.distance_min)/44))].distance.count()


        self.distance_total = [
            [
                (data.iloc[int(self.count_total / 740)].distance),
                (data.iloc[int(self.count_total / 44)].distance),
                (data.iloc[int(self.count_total / 6)].distance),
                (data.iloc[int(self.count_total / 2)].distance),
                (data.iloc[int(self.count_total * 5 / 6)].distance),
                (data.iloc[int(self.count_total * 43 / 44)].distance),
                (data.iloc[int(self.count_total * 739 / 740)].distance)
            ],
            [
                (data.loc[data['distance'] < (self.distance_min + ((self.distance_max - self.distance_min) / 740))].distance.count()) * self.distance_max / self.count_total,
                (data.loc[data['distance'] < (self.distance_min + ((self.distance_max - self.distance_min) / 44))].distance.count()) * self.distance_max / self.count_total,
                (data.loc[data['distance'] < (self.distance_min + ((self.distance_max - self.distance_min) / 6))].distance.count()) * self.distance_max / self.count_total,
                (data.loc[data['distance'] < (self.distance_min + ((self.distance_max - self.distance_min) / 2))].distance.count()) * self.distance_max / self.count_total,
                (data.loc[data['distance'] > (self.distance_min + ((self.distance_max - self.distance_min) * 5 / 6))].distance.count()) * self.distance_max / self.count_total,
                (data.loc[data['distance'] > (self.distance_min + ((self.distance_max - self.distance_min) * 43 / 44))].distance.count()) * self.distance_max / self.count_total,
                (data.loc[data['distance'] > (self.distance_min + ((self.distance_max - self.distance_min) * 739 / 740))].distance.count()) * self.distance_max / self.count_total
            ]
        ]
        self.distance_same = [
            [
                0,
                2,
                3.5,
                4,
                8,
                3,
                4,
                6,
                2,
                6
            ],
            [0, 6, 5.5, 3, 3, 11, 7, 4, 7, 9]
        ]
        self.distance_similar = [
            [0, 2, 3.5, 4, 8, 3, 4, 6, 2, 6, 4.7, 3, 5],
            [0, 6, 5.5, 3, 3, 11, 7, 4, 7, 9, 10, 12, 13]
        ]

        self.distance_top = [
            data.head(n=8).distance[0],
            data.head(n=8).distance[1],
            data.head(n=8).distance[2],
            data.head(n=8).distance[3],
            data.head(n=8).distance[4],
            data.head(n=8).distance[5],
            data.head(n=8).distance[6],
            data.head(n=8).distance[7]
        ]
        self.distance_similar_b = [
            data.iloc[int(self.count_similar * 1 / 8)].distance,
            data.iloc[int(self.count_similar * 2 / 8)].distance,
            data.iloc[int(self.count_similar * 3 / 8)].distance,
            data.iloc[int(self.count_similar * 4 / 8)].distance,
            data.iloc[int(self.count_similar * 5 / 8)].distance,
            data.iloc[int(self.count_similar * 6 / 8)].distance,
            data.iloc[int(self.count_similar * 7 / 8)].distance,
            data.iloc[int(self.count_similar)].distance
        ]
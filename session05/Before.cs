using System;
using System.Collections.Generic;
using System.Linq;

namespace BeforeAndAfter.Before {

    public class ArticleStatus {
        public int Id { get; set; }
        public string Name { get; set; }
    }

    public class Article {
        public bool? HiddenByReviewer { get; set; }
        public ArticleStatus Status { get; set; }
        public long ReviewCode { get; set; }
        public string Name { get; set; }
    }

    public class UserFilter {
        public string Value { get; set; }
        public string Logic { get; set; }
        public string Operator { get; set; }
    }
    
    public enum Tab {
        WorkInProgress,
        SubmittedForReview,
        Accepted,
        Completed
    }

    public class Exercise {

        public IEnumerable<Article> FilterProposals(IEnumerable<Article> dataToFilter, UserFilter filter, Tab tab)
        {
            IEnumerable<Article> filteredData = null;

            switch (tab) {
                case Tab.Accepted:
                    filteredData = dataToFilter.Where(p => !p.HiddenByReviewer.HasValue || !p.HiddenByReviewer.Value);
                    break;
                case Tab.Completed:
                    filteredData = (
                        dataToFilter.Where(
                            p => (
                                (p.HiddenByReviewer.HasValue == true && p.HiddenByReviewer.Value == true) ||
                                (p.Status != null && p.Status.Id == 9)
                        
                            )    
                        )
                    );
                    break;
                default:
                    break;
            }

            if (filter != null && !string.IsNullOrEmpty(filter.Value))
            {
                var tmpData = filteredData ?? dataToFilter;

                if (filter.Logic.Equals("or") && filter.Operator.Equals("contains"))
                {
                    switch (tab)
                    {
                        case Tab.Accepted:
                        case Tab.Completed:
                            filteredData = tmpData.Where(t => t.Name.IndexOf(filter.Value, StringComparison.OrdinalIgnoreCase) >= 0 ||
                            string.Format("THING#{0}", t.ReviewCode.ToString().PadLeft(10, '0')).IndexOf(filter.Value, StringComparison.OrdinalIgnoreCase) >= 0);
                            break;
                        default:
                            break;
                    }
                }
            }

            return filteredData;
        }

    }
}